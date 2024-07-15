# Slides for the gem5 bootcamp

In this directory, you will find the slides that we use during the gem5 bootcamp and gem5 tutorials.
They are written using [Marp](https://marp.app/), a Markdown-based slide design tool.

We chose to use Markdown for slides to make it easier for us to update the code in the slides as gem5 changes and for the participants to copy-paste code.

To use Marp, we encourage you to install the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode), which should be automatically installed if you're using the codespaces devcontainer.
With the VS Code extension installed, when you open one of the slide decks (e.g., [Getting started](02-Using gem5/00-getting-started.md)), you can click on the preview button in the upper right to view the slides.
Also, you can use the Marp extension to save the slides as HTML or PDF.

For using the Marp command line, you can use the following command (pass in the file to convert).
Note: The local paths for the css file and the markdown don't work great. YMMV.

```sh
docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER=$UID:$GID -e LANG=$LANG marpteam/marp-cli <markdown file>
```

## Style rules

- INSTALL THE [MARKDOWN LINT EXTENSION IN VS CODE](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) TO HELP WITH FORMATTING.
- Use `---` to separate slides.
- The first slide should be a "title" slide `<!-- _class: title -->`.
- The titles of all slides should be heading 2 `##`
- Code should be at most 65 characters wide.
- One line per sentence in Markdown.
- Do not use inline HTML unless *absolutely* necessary.
- Images should use markdown syntax `![alt text](path/to/image.png)`

### Layouts

To use a different layout, you specify a class in the markdown file.

```md
<!-- _class: <layout> -->
```

Here are some of the available layouts:

- `title`: Title slide
- `twoCol`: Two columns. To split the slide into two columns, use `###` (heading 3) to create a new column.
- `center-image`: Centers images horizontally

## Adding diagrams

To add diagrams, you can use the [draw.io VS Code extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio).

After installing the extension, create a file with the name "\<name\>.drawio.png" and open it in VS Code.
Make sure you create a directory for each slide deck with its images.
You can then embed the image in the slide with the following markdown.

```md
![<description of the image>](<current slide name>/<name>.drawio.png)
```

## Improvement to make

- [ ] Fix `[bg left]` `[bg right]` in the slides so that the gem5 logo at the bottom doesn't move
- [ ] Extend marp to support [asciinema](https://github.com/asciinema/asciinema-player/releases/tag/v3.8.0)
  - We could [embed an SVG](https://docs.asciinema.org/manual/server/embedding/#preview-image-link).
- [ ] Can we possibly make it so that there's a button to copy the code examples?
