import React from 'react';
import { classes, compile } from 'core/js/reactHelpers';

/**
 * ab-hero component template.
 *
 * Renders a single .ab.hero object. All hero visuals (fill, layout, media
 * placement, entrance) come from the .ab.hero system (ab-base-hero.less / the
 * brand ab-hero.less); this template only supplies structure and the chosen
 * modifier classes. Actions reuse the .ab.btn object.
 */
export default function Hero(props) {
  const {
    _variant,
    _align,
    _animate,
    _icon,
    eyebrow,
    heading,
    body,
    _media,
    _ctas
  } = props;

  const media = _media || {};
  const ctas = _ctas || [];

  const hasIcon = !!_icon;
  const placement = media._placement || 'none';
  const hasSideMedia = placement === 'side' && (media.src || media.poster);
  const hasBgMedia = placement === 'background' && (media.src || media.poster);

  const heroClasses = classes([
    'ab', 'hero',
    _variant || 'neutral',
    _align === 'center' && 'center',
    _animate && 'animate',
    hasIcon && 'icon-text',
    hasSideMedia && 'media-side',
    hasBgMedia && 'media-bg'
  ]);

  return (
    <div className="component__inner ab-hero__inner">
      <div className="component__widget ab-hero__widget">
        <div className={heroClasses}>

          {hasBgMedia && (
            <div className="hero-bg">
              <Media media={media} />
            </div>
          )}

          {hasIcon && (
            <span className={classes(['hero-icon', 'icon', _icon])} aria-hidden="true" />
          )}

          {!!eyebrow && <p className="hero-eyebrow">{eyebrow}</p>}
          {!!heading && (
            <h2
              className="hero-title"
              dangerouslySetInnerHTML={{ __html: compile(heading) }}
            />
          )}
          {!!body && (
            <div
              className="hero-subtitle"
              dangerouslySetInnerHTML={{ __html: compile(body) }}
            />
          )}

          {ctas.length > 0 && (
            <div className="hero-actions">
              {ctas.map((cta, index) => (
                <a
                  key={index}
                  className={classes(['ab', 'btn', cta._variant || 'accent', cta._outline && 'outline'])}
                  href={cta.url}
                >
                  {cta.text || cta.url}
                </a>
              ))}
            </div>
          )}

          {hasSideMedia && (
            <div className="hero-media">
              <Media media={media} />
            </div>
          )}

        </div>
      </div>
    </div>
  );
}

/**
 * The hero media element (image or video).
 */
function Media({ media }) {
  if (media._type === 'video') {
    return (
      <video src={media.src} poster={media.poster || ''} controls={!!media._controls} muted playsInline />
    );
  }
  return <img src={media.src} alt={media.alt || ''} />;
}
