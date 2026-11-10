import Adapt from 'core/js/adapt';
import QuestionView from 'core/js/views/questionView';

/**
 * SortableView - Accessible drag-and-drop + keyboard reordering question component
 *
 * Accessibility approach:
 * - Each item is focusable (tabindex=0) and has role="option" within a role="listbox"
 * - Keyboard: Arrow Up/Down moves the focused item; Enter/Space toggles "grabbed" state
 * - Move buttons: Each item has up/down buttons for explicit move actions
 * - ARIA live region announces moves: "{item} moved to position {n} of {total}"
 * - Drag-and-drop: Standard HTML5 drag events for mouse/touch users
 * - Focus management: Focus follows the moved item
 */
class SortableView extends QuestionView {

  events() {
    return {
      // Mouse/touch drag events
      'dragstart .js-grow-sortable-item': 'onDragStart',
      'dragover .js-grow-sortable-item': 'onDragOver',
      'dragenter .js-grow-sortable-item': 'onDragEnter',
      'dragleave .js-grow-sortable-item': 'onDragLeave',
      'drop .js-grow-sortable-item': 'onDrop',
      'dragend .js-grow-sortable-item': 'onDragEnd',

      // Move button clicks
      'click .js-grow-sortable-move-up': 'onMoveUpClick',
      'click .js-grow-sortable-move-down': 'onMoveDownClick',

      // Keyboard events on items
      'keydown .js-grow-sortable-item': 'onItemKeydown'
    };
  }

  initialize(...args) {
    super.initialize(...args);
    this.draggedItem = null;
    this.draggedIndex = null;
    this.isGrabbed = false; // For keyboard "grabbed" state

    // Listen for model events - use changed() not render() to avoid re-triggering
    // PageLevelProgress indicator creation
    this.listenTo(this.model, 'sortable:orderChanged', this.onOrderChanged);
    this.listenTo(this.model, 'sortable:reset', this.onReset);
    this.listenTo(this.model, 'sortable:showCorrectAnswer', this.changed);
    this.listenTo(this.model, 'sortable:showUserAnswer', this.changed);
  }

  setupQuestion() {
    this.model.setUpItems();
  }

  onQuestionRendered() {
    this.setReadyStatus();
  }

  // ==================
  // DRAG AND DROP
  // ==================

  onDragStart(event) {
    if (!this.model.get('_isEnabled')) return;

    const item = event.currentTarget;
    this.draggedItem = item;
    this.draggedIndex = parseInt(item.dataset.displayIndex, 10);

    // Set drag data
    event.originalEvent.dataTransfer.effectAllowed = 'move';
    event.originalEvent.dataTransfer.setData('text/plain', this.draggedIndex.toString());

    // Add dragging class after a small delay (for visual feedback)
    setTimeout(() => {
      item.classList.add('is-dragging');
    }, 0);
  }

  onDragOver(event) {
    if (!this.model.get('_isEnabled') || !this.draggedItem) return;
    event.preventDefault();
    event.originalEvent.dataTransfer.dropEffect = 'move';
  }

  onDragEnter(event) {
    if (!this.model.get('_isEnabled') || !this.draggedItem) return;
    const target = event.currentTarget;
    if (target !== this.draggedItem) {
      target.classList.add('is-drag-over');
    }
  }

  onDragLeave(event) {
    const target = event.currentTarget;
    target.classList.remove('is-drag-over');
  }

  onDrop(event) {
    if (!this.model.get('_isEnabled') || !this.draggedItem) return;
    event.preventDefault();

    const target = event.currentTarget;
    target.classList.remove('is-drag-over');

    const fromIndex = this.draggedIndex;
    const toIndex = parseInt(target.dataset.displayIndex, 10);

    if (fromIndex !== toIndex) {
      this.moveItemAndAnnounce(fromIndex, toIndex);
    }
  }

  onDragEnd(event) {
    if (this.draggedItem) {
      this.draggedItem.classList.remove('is-dragging');
    }
    this.draggedItem = null;
    this.draggedIndex = null;

    // Clean up any remaining drag-over states
    this.$('.js-grow-sortable-item').removeClass('is-drag-over');
  }

  // ==================
  // MOVE BUTTONS
  // ==================

  onMoveUpClick(event) {
    if (!this.model.get('_isEnabled')) return;
    event.preventDefault();
    event.stopPropagation();

    const button = event.currentTarget;
    const displayIndex = parseInt(button.dataset.displayIndex, 10);

    if (displayIndex > 0) {
      this.moveItemAndAnnounce(displayIndex, displayIndex - 1);
    }
  }

  onMoveDownClick(event) {
    if (!this.model.get('_isEnabled')) return;
    event.preventDefault();
    event.stopPropagation();

    const button = event.currentTarget;
    const displayIndex = parseInt(button.dataset.displayIndex, 10);
    const totalItems = this.model.get('_displayItems').length;

    if (displayIndex < totalItems - 1) {
      this.moveItemAndAnnounce(displayIndex, displayIndex + 1);
    }
  }

  // ==================
  // KEYBOARD NAVIGATION
  // ==================

  onItemKeydown(event) {
    if (!this.model.get('_isEnabled')) return;

    const item = event.currentTarget;
    const displayIndex = parseInt(item.dataset.displayIndex, 10);
    const totalItems = this.model.get('_displayItems').length;

    switch (event.key) {
      case 'ArrowUp':
      case 'Up':
        event.preventDefault();
        if (this.isGrabbed) {
          // Move item up
          if (displayIndex > 0) {
            this.moveItemAndAnnounce(displayIndex, displayIndex - 1);
          }
        } else {
          // Move focus up
          this.focusItemAtIndex(displayIndex - 1);
        }
        break;

      case 'ArrowDown':
      case 'Down':
        event.preventDefault();
        if (this.isGrabbed) {
          // Move item down
          if (displayIndex < totalItems - 1) {
            this.moveItemAndAnnounce(displayIndex, displayIndex + 1);
          }
        } else {
          // Move focus down
          this.focusItemAtIndex(displayIndex + 1);
        }
        break;

      case 'Enter':
      case ' ':
        event.preventDefault();
        this.toggleGrabbed(item);
        break;

      case 'Escape':
        if (this.isGrabbed) {
          event.preventDefault();
          this.releaseGrabbed(item);
        }
        break;

      case 'Home':
        event.preventDefault();
        if (this.isGrabbed && displayIndex > 0) {
          this.moveItemAndAnnounce(displayIndex, 0);
        } else if (!this.isGrabbed) {
          this.focusItemAtIndex(0);
        }
        break;

      case 'End':
        event.preventDefault();
        if (this.isGrabbed && displayIndex < totalItems - 1) {
          this.moveItemAndAnnounce(displayIndex, totalItems - 1);
        } else if (!this.isGrabbed) {
          this.focusItemAtIndex(totalItems - 1);
        }
        break;
    }
  }

  toggleGrabbed(item) {
    if (this.isGrabbed) {
      this.releaseGrabbed(item);
    } else {
      this.isGrabbed = true;
      item.classList.add('is-grabbed');
      item.setAttribute('aria-grabbed', 'true');
      this.announceToScreenReader('Item selected. Use arrow keys to move, Enter to drop.');
    }
  }

  releaseGrabbed(item) {
    this.isGrabbed = false;
    item.classList.remove('is-grabbed');
    item.setAttribute('aria-grabbed', 'false');
    this.announceToScreenReader('Item released.');
  }

  focusItemAtIndex(index) {
    const items = this.$('.js-grow-sortable-item');
    const totalItems = items.length;

    // Clamp index to valid range
    const targetIndex = Math.max(0, Math.min(index, totalItems - 1));
    const targetItem = items.eq(targetIndex);

    if (targetItem.length) {
      targetItem.focus();
    }
  }

  // ==================
  // MOVE AND ANNOUNCE
  // ==================

  moveItemAndAnnounce(fromIndex, toIndex) {
    const displayItems = this.model.get('_displayItems');
    const movedItem = displayItems[fromIndex];
    const totalItems = displayItems.length;

    // Perform the move in the model
    this.model.moveItem(fromIndex, toIndex);

    // Announce to screen reader
    const globals = Adapt.course.get('_globals')?._components?._growSortable || {};
    const ariaTemplate = globals.ariaItemMoved || '{{{itemText}}} moved to position {{{position}}} of {{{total}}}';
    const announcement = Handlebars.compile(ariaTemplate)({
      itemText: movedItem.text,
      position: toIndex + 1,
      total: totalItems
    });
    this.announceToScreenReader(announcement);
  }

  onOrderChanged({ fromIndex, toIndex, displayItems }) {
    // Re-render to reflect new order - use changed() not render()
    // to avoid re-triggering PageLevelProgress indicator creation
    this.changed();

    // Focus the moved item at its new position
    this.$nextTick(() => {
      this.focusItemAtIndex(toIndex);

      // Maintain grabbed state if active
      if (this.isGrabbed) {
        const item = this.$('.js-grow-sortable-item').eq(toIndex);
        item.addClass('is-grabbed');
        item.attr('aria-grabbed', 'true');
      }
    });
  }

  onReset() {
    this.isGrabbed = false;
    // Use changed() not render() to avoid PageLevelProgress issues
    this.changed();
  }

  // ==================
  // ARIA LIVE REGION
  // ==================

  announceToScreenReader(message) {
    const liveRegion = this.$(`#${this.model.get('_id')}-grow-sortable-live`);
    // Clear then set to ensure announcement
    liveRegion.text('');
    setTimeout(() => {
      liveRegion.text(message);
    }, 50);
  }

  // ==================
  // UTILITY
  // ==================

  $nextTick(callback) {
    // Wait for DOM update
    setTimeout(callback, 0);
  }

  // Override showCorrectAnswer from QuestionView
  showCorrectAnswer() {
    this.model.showCorrectAnswer();
  }

  // Override showUserAnswer (hideCorrectAnswer) from QuestionView
  hideCorrectAnswer() {
    this.model.showUserAnswer();
  }

}

SortableView.template = 'growSortable.jsx';

export default SortableView;
