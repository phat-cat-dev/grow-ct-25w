# Projects in this repo

This folder (`adapt-forks/grow-course/`, formerly `adapt3`; the working tree is
`wkspc2614-adapt3/`) holds **two logical projects that share one Adapt Framework
tree**. They can't be split into separate folders without breaking the Adapt
build (Adapt requires `src/`, `grunt/`, `Gruntfile.js` at the root), so this is
an *overview layer*, not a physical split.

| Project | What it is | Overview |
|---|---|---|
| **GROW-BUILD** | The Adapt Framework build — compiles a course into a playable / SCORM package. | [docs/projects/GROW-BUILD.md](docs/projects/GROW-BUILD.md) |
| **GROW-CONTEXT** | The gate→manifest authoring engine — turns design decisions into course source. | [docs/projects/GROW-CONTEXT.md](docs/projects/GROW-CONTEXT.md) |

Working note:
- [docs/projects/GROW-CT-IMPORT.md](docs/projects/GROW-CT-IMPORT.md) — plan to bring the styling / components built in the sibling `grow-ct` repo into this build.

**One-line flow:** GROW-CONTEXT produces a course under `courses/<slug>/` → the
`src/course` symlink points the build at it → GROW-BUILD (`grunt build`) compiles
it to `build/` → `package-scorm.js` zips it to `scorm-packages/`.

The engine (GROW-CONTEXT) could later be lifted out to its own standalone repo —
see GROW-CONTEXT.md "Standalone" — but today it lives here alongside the build,
which is the decision recorded for now: **one working space, build + author in place.**
