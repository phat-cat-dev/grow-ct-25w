import React from 'react';
import { templates, compile } from 'core/js/reactHelpers';

/**
 * Annotate template — a static shell. The view wires interaction and the
 * grow-marks engine imperatively after render (no React re-render, so the
 * appended mark SVGs survive).
 *
 *  - palette : one button per annotation tool (role=toolbar). The view draws
 *    each tool's own mark over its label as a preview.
 *  - passage : author text parsed into segments; targets are <button>s the
 *    learner annotates.
 */
export default function Annotate(props) {
  const {
    _id,
    _tools = [],
    _segments = [],
    _allowReset,
    instruction
  } = props;

  return (
    <div className="component__inner annotate__inner">

      <templates.header {...props} />

      {instruction && (
        <div className="annotate__instruction" dangerouslySetInnerHTML={{ __html: compile(instruction) }} />
      )}

      <div className="component__widget annotate__widget">

        <div className="annotate__palette" role="toolbar" aria-label="Annotation tools">
          {_tools.map(tool => (
            <button
              key={tool._id}
              type="button"
              className="annotate__tool"
              data-tool={tool._id}
              aria-pressed="false"
            >
              <span className="annotate__tool-label">{tool.label}</span>
            </button>
          ))}
        </div>

        <p className="annotate__passage">
          {_segments.map((seg, index) => (
            seg.type === 'target' ? (
              <button
                key={index}
                type="button"
                className="annotate__target"
                data-key={seg.key}
                aria-pressed="false"
              >
                {seg.text}
              </button>
            ) : (
              <span key={index} dangerouslySetInnerHTML={{ __html: compile(seg.text) }} />
            )
          ))}
        </p>

        <div className="annotate__footer">
          {_allowReset !== false && (
            <button type="button" className="annotate__reset btn-text">Clear annotations</button>
          )}
          <span className="annotate__status" role="status" aria-live="polite" />
        </div>

      </div>

    </div>
  );
}
