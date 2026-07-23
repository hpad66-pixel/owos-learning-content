# Three persistent lesson actions

Date: 2026-07-23

## Hardeep direction

Every course landing page and lesson must show Graph, Community, and Start at the top. Graph and Community must also remain available in the complete connected-learning section at the bottom.

Graph and Community open responsive side drawers without taking the learner away from the course. Start moves directly to the beginning of the lesson. The three top actions must exist in the source HTML and must not depend on delayed runtime injection.

## Implementation decision

- Add Graph, Community, and Start to the source header of the landing page and all eight modules.
- Keep the shared runtime enhancement for the responsive Graph and Community drawers.
- Keep the explicit bottom connected-learning anchor before lesson navigation.
- Add automated checks so no future release can omit any of the three top actions.
