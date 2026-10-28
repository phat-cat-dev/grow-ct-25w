import { Fragment } from "react";

const DEFAULT_META = [
  "Single-hue foundations",
  "Live font & symbol connectors",
  "Portable CSS",
];

export default function Header({
  eyebrow = "AB / Design system workbench",
  titleLines = ["One system.", "A world of possibilities."],
  description = "Shape a coherent visual language. Explore colour, pair type, collect symbols and build a scheme that is yours.",
  meta = DEFAULT_META,
}) {
  return (
    <header className="ab-header">
      <span className="ab-header__eyebrow">{eyebrow}</span>
      <h1 className="ab-header__title">
        {titleLines.map((line, index) => (
          <Fragment key={`${index}-${line}`}>
            {index > 0 && <br />}
            {line}
          </Fragment>
        ))}
      </h1>
      <p className="ab-header__description">{description}</p>
      {meta.length > 0 && (
        <ul className="ab-header__meta" aria-label="Header highlights">
          {meta.map((item) => (
            <li className="ab-header__meta-item" key={item}>
              {item}
            </li>
          ))}
        </ul>
      )}
    </header>
  );
}
