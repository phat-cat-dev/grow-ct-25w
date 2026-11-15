import React from 'react';
import { templates } from 'core/js/reactHelpers';

export default function growGuidedChat(props) {
  const chat = props._chat || {};
  const messages = chat._messages || [];
  const labels = chat._labels || {};
  return (
    <div className="component__inner grow-guided-chat__inner">
      <templates.header {...props} />
      <div className="component__widget grow-guided-chat">
        <ol className="grow-guided-chat__messages" aria-label="Scripted conversation">
          {messages.map((message, index) => {
            const speaker = message._speaker === 'learner' ? 'learner' : 'guide';
            const name = message.name
              || (speaker === 'learner' ? (chat.learnerName || 'Learner') : (chat.guideName || 'Guide'));
            return (
              <li key={index} className="grow-guided-chat__bubble" data-speaker={speaker} data-text={message.text} hidden>
                <strong className="grow-guided-chat__speaker">{name}</strong>
                <span className="grow-guided-chat__sr">{message.text}</span>
                <span className="grow-guided-chat__typed" aria-hidden="true" />
              </li>
            );
          })}
        </ol>
        <div className="grow-guided-chat__controls">
          <button type="button" data-chat="next" disabled>{labels.next || 'Next message'}</button>
          <button type="button" data-chat="skip" disabled>{labels.skip || 'Show full message'}</button>
          <button type="button" data-chat="replay">{labels.replay || 'Replay conversation'}</button>
        </div>
        <p className="grow-guided-chat__status" role="status" aria-live="polite" />
      </div>
    </div>
  );
}
