Here is the proposed document pipeline:

```mermaid
graph TD
    A[Raw Notes] --> B(Markdown Editor)
    B --> C{Output Type?}
    C -->|Internal| D[Marp Preview]
    C -->|Corporate| E[Pandoc Compile]
    D --> F[PDF Export]
    E --> G[PPTX File]
