import ComponentView from 'core/js/views/componentView';

// A cork-board of sticky notes. In 'display' mode it renders authored notes
// (text). In 'brainstorm' mode each note shows an author title and an editable
// text area the learner fills (vocabulary / terminology / questions); entries
// persist via the model and completion is set once enough notes are filled.
class CorkboardView extends ComponentView {

  events() {
    return {
      'input .grow-corkboard__input': 'onInput',
      'blur .grow-corkboard__input': 'onBlur'
    };
  }

  preRender() {
    // normalise notes once so the template stays declarative
    const notes = (this.model.get('_notes') || []).map((note, index) => ({
      text: typeof note.text === 'string' ? note.text : '',
      title: typeof note.title === 'string' ? note.title : '',
      _placeholder: typeof note._placeholder === 'string' ? note._placeholder : '',
      _color: note._color || 'default',
      // a gentle default jitter when the author leaves rotation unset
      _rotation: Number.isFinite(Number(note._rotation)) ? Number(note._rotation) : ((index % 2 ? 1 : -1) * (1 + (index % 3)))
    }));
    // show only the chosen number of notes
    this.model.set('_notes', notes.slice(0, this.model.getVisibleCount() || notes.length));
  }

  postRender() {
    this._debouncedSave = _.debounce(this._save.bind(this), 1500, { maxWait: 10000 });
    // repopulate inputs from any restored entries (restore may land after render)
    if (this.model.get('_mode') === 'brainstorm') {
      const entries = this.model.getEntries();
      this.$('.grow-corkboard__input').each((idx, el) => {
        const i = Number(el.getAttribute('data-index'));
        if (entries[i] != null && el.value !== entries[i]) el.value = entries[i];
      });
    }
    this.setReadyStatus();
  }

  onInput(event) {
    const el = event.currentTarget;
    this.model.setEntry(Number(el.getAttribute('data-index')), el.value);
    this._debouncedSave();
    this.model.checkCompletion();
  }

  onBlur() {
    if (this._debouncedSave) this._debouncedSave.cancel();
    this._save();
    this.model.checkCompletion();
  }

  _save() {
    this.model.saveEntries();
  }

  remove() {
    if (this._debouncedSave) this._debouncedSave.cancel();
    super.remove();
  }

}

CorkboardView.template = 'growCorkboard.jsx';

export default CorkboardView;
