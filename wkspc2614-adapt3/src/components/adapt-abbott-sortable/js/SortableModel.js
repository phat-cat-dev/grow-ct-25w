import Adapt from 'core/js/adapt';
import ItemsQuestionModel from 'core/js/models/itemsQuestionModel';
import ItemModel from 'core/js/models/itemModel';

export default class SortableModel extends ItemsQuestionModel {

  /**
   * Set up the items for the sortable component.
   * Items are authored in CORRECT order; we store that order and then shuffle for display.
   * Uses setChildren() to properly register items (like Matching does) to avoid
   * PageLevelProgress creating multiple indicators.
   */
  setUpItems() {
    const items = this.get('_items') || [];

    // Store the correct order (authored order = correct order)
    // Each item gets its correct position (0-indexed)
    items.forEach((item, index) => {
      item._correctPosition = index;
      item._index = index;
    });

    // Store the correct order for later comparison
    this.set('_correctOrder', items.map(item => item._index));

    // Shuffle items for display (Fisher-Yates shuffle)
    const shuffled = this.shuffleItems([...items]);

    // Track the current display order (will be updated as user reorders)
    this.set('_currentOrder', shuffled.map(item => item._index));
    this.set('_displayItems', shuffled);
    this.set({
      _items: items,
      _selectable: items.length
    });

    // Register items as children using setChildren() - this ensures proper framework
    // integration and prevents PageLevelProgress from treating items as separate trackables
    this.setChildren(new Backbone.Collection(items, { model: ItemModel }));
  }

  /**
   * Fisher-Yates shuffle
   */
  shuffleItems(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  /**
   * Move an item from one position to another
   * @param {number} fromIndex - Current position in display order
   * @param {number} toIndex - Target position in display order
   */
  moveItem(fromIndex, toIndex) {
    const displayItems = [...this.get('_displayItems')];
    const [movedItem] = displayItems.splice(fromIndex, 1);
    displayItems.splice(toIndex, 0, movedItem);

    this.set('_displayItems', displayItems);
    this.set('_currentOrder', displayItems.map(item => item._index));

    // Trigger event for view to update
    this.trigger('sortable:orderChanged', { fromIndex, toIndex, displayItems });
  }

  /**
   * Check if user can submit (always true for sortable - order is always defined)
   */
  canSubmit() {
    return true;
  }

  /**
   * Store the user's answer for restoration
   */
  storeUserAnswer() {
    const currentOrder = this.get('_currentOrder');
    this.set('_userAnswer', [...currentOrder]);
  }

  /**
   * Restore user's previous answer
   */
  restoreUserAnswers() {
    if (!this.get('_isSubmitted')) return;

    const userAnswer = this.get('_userAnswer');
    if (!userAnswer) return;

    // Restore the display order from saved answer
    const items = this.get('_items');
    const displayItems = userAnswer.map(index => items.find(item => item._index === index));

    this.set('_displayItems', displayItems);
    this.set('_currentOrder', userAnswer);

    this.setQuestionAsSubmitted();
    this.markQuestion();
    this.setScore();
    this.setupFeedback();
  }

  /**
   * Check if the answer is correct.
   * All-or-nothing: all items must be in their correct positions.
   */
  isCorrect() {
    const correctOrder = this.get('_correctOrder');
    const currentOrder = this.get('_currentOrder');

    // Count correct positions
    let correctCount = 0;
    for (let i = 0; i < correctOrder.length; i++) {
      if (currentOrder[i] === correctOrder[i]) {
        correctCount++;
      }
    }

    this.set('_numberOfCorrectPositions', correctCount);
    this.set('_numberOfRequiredPositions', correctOrder.length);

    // All-or-nothing: all positions must match
    return correctCount === correctOrder.length;
  }

  /**
   * Partly correct if some items are in the right position but not all.
   * (For future partial credit support)
   */
  isPartlyCorrect() {
    const correctCount = this.get('_numberOfCorrectPositions') || 0;
    const total = this.get('_numberOfRequiredPositions') || 0;
    return correctCount > 0 && correctCount < total;
  }

  /**
   * Set score (all-or-nothing for now)
   */
  setScore() {
    const questionWeight = this.get('_questionWeight');
    const isCorrect = this.get('_isCorrect');
    this.set('_score', isCorrect ? questionWeight : 0);
  }

  /**
   * Reset the question for another attempt
   */
  resetQuestion() {
    // Re-shuffle items
    const items = this.get('_items') || [];
    const shuffled = this.shuffleItems([...items]);
    this.set('_displayItems', shuffled);
    this.set('_currentOrder', shuffled.map(item => item._index));
    this.trigger('sortable:reset');
  }

  /**
   * Reset user answer
   */
  resetUserAnswer() {
    this.set('_userAnswer', []);
  }

  /**
   * Show the correct order (for model answer display)
   */
  showCorrectAnswer() {
    const items = this.get('_items');
    const correctOrder = this.get('_correctOrder');
    const displayItems = correctOrder.map(index => items.find(item => item._index === index));

    this.set('_displayItems', displayItems);
    this.set('_isCorrectAnswerShown', true);
    this.trigger('sortable:showCorrectAnswer');
  }

  /**
   * Restore user's answer (hide correct answer)
   */
  showUserAnswer() {
    const userAnswer = this.get('_userAnswer');
    const items = this.get('_items');
    const displayItems = userAnswer.map(index => items.find(item => item._index === index));

    this.set('_displayItems', displayItems);
    this.set('_isCorrectAnswerShown', false);
    this.trigger('sortable:showUserAnswer');
  }

  /**
   * Get interaction object for SCORM reporting.
   * Uses 'sequencing' type for ordering questions.
   */
  getInteractionObject() {
    const items = this.get('_items') || [];
    const correctOrder = this.get('_correctOrder') || [];

    return {
      correctResponsesPattern: [
        // Format: "1[,]2[,]3[,]4[,]5" (1-indexed positions)
        correctOrder.map(index => String(index + 1)).join('[,]')
      ],
      choices: items.map((item, index) => ({
        id: String(index + 1),
        description: item.text
      }))
    };
  }

  /**
   * Get the user's response for SCORM.
   */
  getResponse() {
    const currentOrder = this.get('_currentOrder') || [];
    // Return comma-separated 1-indexed positions
    return currentOrder.map(index => String(index + 1)).join(',');
  }

  /**
   * Get response type for SCORM (sequencing for ordering questions)
   */
  getResponseType() {
    return 'sequencing';
  }

  /**
   * Get correct answer as text for screen reader
   */
  getCorrectAnswerAsText() {
    const globals = Adapt.course.get('_globals')._components._sortable;
    const ariaTemplate = globals?.ariaCorrectAnswer;
    if (!ariaTemplate) return '';

    const items = this.get('_items');
    const correctOrder = this.get('_correctOrder');
    const correctAnswerText = correctOrder
      .map(index => items.find(item => item._index === index)?.text)
      .filter(Boolean)
      .join(', ');

    return Handlebars.compile(ariaTemplate)({ correctAnswer: correctAnswerText });
  }

  /**
   * Get user's answer as text for screen reader
   */
  getUserAnswerAsText() {
    const globals = Adapt.course.get('_globals')._components._sortable;
    const ariaTemplate = globals?.ariaUserAnswer;
    if (!ariaTemplate) return '';

    const items = this.get('_items');
    const userAnswer = this.get('_userAnswer') || this.get('_currentOrder');
    const userAnswerText = userAnswer
      .map(index => items.find(item => item._index === index)?.text)
      .filter(Boolean)
      .join(', ');

    return Handlebars.compile(ariaTemplate)({ userAnswer: userAnswerText });
  }

}
