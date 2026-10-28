import React from 'react';
import { templates, classes, compile } from 'core/js/reactHelpers';

/**
 * Branching component template.
 *
 * Accessibility model (BB-4):
 * - Choices in a group with role="group" and aria-labelledby
 * - Each choice is a native <button>
 * - After commit-selection, unchosen buttons use aria-disabled="true" (NOT disabled)
 *   Reason: disabled removes from tab order, but unchosen options are meaningful record
 *   in a decision scenario — users should be able to read back what they didn't choose
 * - Chosen button has aria-pressed="true" plus visible marker
 * - Consequence region has tabindex="-1" for programmatic focus move
 * - Focus moves to consequence on selection (BR-5)
 */
export default function Branching(props) {
  const {
    _id,
    _isEnabled,
    _selectionBehaviour,
    instruction,
    _items
  } = props;

  const items = _items || [];
  const behaviour = _selectionBehaviour || 'commit';

  // Check if any item is selected (for commit-lock state)
  const hasSelection = items.some(item => item._isSelected);

  // Find the selected item for consequence display
  const selectedItem = items.find(item => item._isSelected);

  // Generate unique ID for instruction (for aria-labelledby)
  const instructionId = `${_id}-instruction`;

  return (
    <div className="component__inner branching__inner">

      <templates.header {...props} />

      <div className="component__widget branching__widget">

        {/* Instruction as the group label */}
        {instruction && (
          <div
            id={instructionId}
            className="branching__instruction"
            dangerouslySetInnerHTML={{ __html: compile(instruction) }}
          />
        )}

        {/* Choices group */}
        <div
          className="branching__choices"
          role="group"
          aria-labelledby={instruction ? instructionId : undefined}
        >
          {items.map((item, index) => (
            <BranchingChoice
              key={index}
              item={item}
              index={index}
              isEnabled={_isEnabled}
              behaviour={behaviour}
              hasSelection={hasSelection}
            />
          ))}
        </div>

        {/* Consequence region — only visible when a choice is selected */}
        {selectedItem && selectedItem.consequence && (
          <div
            className="branching__consequence"
            tabIndex={-1}
            role="region"
            aria-live="polite"
          >
            {selectedItem.consequence.title && (
              <div className="branching__consequence-title">
                {selectedItem.consequence.title}
              </div>
            )}
            {selectedItem.consequence.body && (
              <div
                className="branching__consequence-body"
                dangerouslySetInnerHTML={{ __html: compile(selectedItem.consequence.body) }}
              />
            )}
          </div>
        )}

      </div>

    </div>
  );
}

/**
 * Individual choice button.
 */
function BranchingChoice({ item, index, isEnabled, behaviour, hasSelection }) {
  const isSelected = !!item._isSelected;
  const isVisited = !!item._isVisited;

  // In commit mode with a selection, unchosen items are aria-disabled
  // (NOT disabled — they stay in tab order so users can read what they didn't choose)
  const isCommitLocked = behaviour === 'commit' && hasSelection && !isSelected;

  // Determine if the button should be interactable
  const isInteractable = isEnabled && !isCommitLocked;

  return (
    <button
      type="button"
      className={classes([
        'branching__choice',
        isSelected && 'is-selected',
        isVisited && 'is-visited',
        isCommitLocked && 'is-commit-locked'
      ])}
      data-index={index}
      aria-pressed={isSelected.toString()}
      aria-disabled={isCommitLocked ? 'true' : undefined}
      disabled={!isEnabled}
    >
      <span className="branching__choice-text">
        {item.text}
      </span>
      {isSelected && (
        <span className="branching__choice-marker" aria-hidden="true">
          &#10003;
        </span>
      )}
    </button>
  );
}
