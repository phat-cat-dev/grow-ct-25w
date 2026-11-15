import React from 'react';
import { compile } from 'core/js/reactHelpers';

/*
  Structure: instruction/body header, a radio-like category palette, a live
  progress counter, then each passage rendered as its pre-resolved segment
  array (`_segments`, built by TextTaggingModel._buildSegments() - never the
  raw `text` + `_taggableSpans` fields directly, and never via `innerHTML`).

  A passage with no `_taggableSpans` resolves to a single non-span segment,
  so it naturally renders as a read-only "contrast passage" here with no
  extra template branching needed.

  Classes prefixed `js-` are behavioural hooks TextTaggingView binds events
  to / queries - do not rename without updating the view. `grow-text-tagging__*`
  (no `js-` prefix) are purely presentational, styled in
  ../less/grow-text-tagging.less. QuestionView fills `.btn__container` and
  manages marking/feedback.
*/
export default function GrowTextTagging(props) {
  const {
    title,
    body,
    instruction,
    _tagCategories,
    _passages
  } = props;

  return (
    <div className="component__inner grow-text-tagging__inner">

      <div className="component__header">
        {title &&
          <h1 className="component__title">{title}</h1>
        }
        {body &&
          <div
            className="component__body"
            dangerouslySetInnerHTML={{ __html: compile(body || '', props) }}
          />
        }
        {instruction &&
          <div
            className="component__instruction"
            dangerouslySetInnerHTML={{ __html: compile(instruction || '', props) }}
          />
        }
      </div>

      <div className="component__widget grow-text-tagging" data-component="growTextTagging">

        <div className="grow-text-tagging__palette" role="group" aria-label="Tag categories">
          {(_tagCategories || []).map((category, index) => (
            <button
              type="button"
              key={index}
              className={`grow-text-tagging__tag-btn grow-text-tagging__tag-btn--tag-${index} js-grow-text-tagging-tag-btn`}
              data-tag-index={index}
              aria-pressed="false"
              tabIndex={0}
              title={category.description || undefined}
            >{category.label}</button>
          ))}
        </div>

        <div className="grow-text-tagging__progress-counter js-grow-text-tagging-progress-counter grow-text-tagging__progress-counter--none">
          <span className="js-grow-text-tagging-tagged-count">0</span> / <span className="js-grow-text-tagging-total-count">0</span> tagged
        </div>

        {(_passages || []).map((passage, pIndex) => (
          <div className="grow-text-tagging__passage" data-passage-id={passage._passageId} key={pIndex}>
            {passage.label &&
              <h3 className="grow-text-tagging__passage-label">{passage.label}</h3>
            }
            <p className="grow-text-tagging__passage-text">
              {(passage._segments || []).map((segment, sIndex) => (
                segment._isSpan
                  ? (
                    <span
                      key={sIndex}
                      className="grow-text-tagging__tag-target js-grow-text-tagging-tag-target"
                      data-span-id={segment._spanId}
                      role="button"
                      tabIndex={0}
                      aria-label={segment.text}
                    >{segment.text}</span>
                  )
                  : <React.Fragment key={sIndex}>{segment.text}</React.Fragment>
              ))}
            </p>
          </div>
        ))}

      </div>

      <ul className="grow-text-tagging__feedback js-grow-text-tagging-feedback" aria-live="polite" hidden></ul>

      <div className="btn__container"></div>

    </div>
  );
}
