import Adapt from 'core/js/adapt';
import ComponentModel from 'core/js/models/componentModel';
import offlineStorage from 'core/js/offlineStorage';
import logging from 'core/js/logging';

/**
 * CorkboardModel
 *
 * Two modes:
 *  - display    : static author notes (text), no state.
 *  - brainstorm : each note has an author title; the learner types an entry.
 *                 Entries persist via offlineStorage (cmi.suspend_data) keyed by
 *                 component _id, restored at adapt:start, mirroring adapt-grow-opentext.
 *                 Completion is set when the required number of notes are filled.
 */
const KEY_PREFIX = 'cb:';

export default class CorkboardModel extends ComponentModel {

  defaults() {
    return {
      ...super.defaults(),
      _mode: 'display',
      _count: 4,
      _minComplete: 0, // 0 = every shown note must be filled
      _entries: []
    };
  }

  init() {
    super.init();
    if (this.get('_mode') === 'brainstorm') {
      this.listenToOnce(Adapt, 'adapt:start', this.restoreEntries);
    }
  }

  getStorageKey() {
    return KEY_PREFIX + this.get('_id');
  }

  /** How many of the authored notes are actually shown (capped by _count). */
  getVisibleCount() {
    const notes = this.get('_notes') || [];
    const count = Number(this.get('_count'));
    return Number.isFinite(count) && count > 0 ? Math.min(count, notes.length) : notes.length;
  }

  getEntries() {
    const entries = this.get('_entries');
    return Array.isArray(entries) ? entries : [];
  }

  getEntry(index) {
    return this.getEntries()[index] || '';
  }

  setEntry(index, text) {
    const entries = this.getEntries().slice();
    entries[index] = text;
    this.set('_entries', entries);
  }

  /** Restore learner entries from offlineStorage. Defensive about shape. */
  restoreEntries() {
    const scorm = Adapt.spoor?.scorm;
    if (!scorm || !scorm.lmsConnected) return;
    let stored;
    try {
      stored = offlineStorage.get(this.getStorageKey());
    } catch (e) {
      logging.warn(`[corkboard] ${this.get('_id')}: error reading offlineStorage: ${e.message}`);
      return;
    }
    if (stored === undefined || stored === null || stored === '') return;
    const entries = (typeof stored === 'object' && Array.isArray(stored.e)) ? stored.e
      : (Array.isArray(stored) ? stored : null);
    if (entries) this.set('_entries', entries);
  }

  /** Save learner entries to offlineStorage. No-op without an LMS. */
  saveEntries() {
    const scorm = Adapt.spoor?.scorm;
    if (!scorm || !scorm.lmsConnected) return { success: false, errorCode: 'NO_LMS' };
    try {
      offlineStorage.set(this.getStorageKey(), { v: 'brainstorm', e: this.getEntries() });
    } catch (e) {
      logging.error(`[corkboard] ${this.get('_id')}: offlineStorage.set threw: ${e.message}`);
      return { success: false, errorCode: e.message };
    }
    return { success: true };
  }

  filledCount() {
    const visible = this.getVisibleCount();
    let filled = 0;
    for (let i = 0; i < visible; i++) if ((this.getEntry(i) || '').trim()) filled++;
    return filled;
  }

  /** How many notes must be filled: _minComplete if valid, else all shown. */
  requiredCount() {
    const min = Number(this.get('_minComplete'));
    const visible = this.getVisibleCount();
    return (Number.isFinite(min) && min > 0 && min <= visible) ? min : visible;
  }

  canComplete() {
    return this.getVisibleCount() > 0 && this.filledCount() >= this.requiredCount();
  }

  /** Completion is sticky — set once the learner has filled enough notes. */
  checkCompletion() {
    if (this.get('_isComplete')) return;
    if (this.get('_mode') === 'brainstorm' && this.canComplete()) this.setCompletionStatus();
  }

}
