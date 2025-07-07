# Manim

## Motivation

Creating animated content is hard. It always takes longer than you want and it
is hard to edit to get right. For technical topics a wrong animation might be
worse than useless, it could actively be misleading and waste people's time.

Classic solution for technical slides is to create multiple static images
and flip (or fade) from one slide to the next to show steps.



## History

Originally designed by [3Blue1Brown](https://www.3blue1brown.com/) YouTuber
Grant Sanderson for creating his math videos.

Project was open sourced by Grant and developed by community. Currently two main
forks, original and community. Original fork is backwards compatible with
scripts from 3b1b code in older videos. Designed to match what is presented in
videos exactly. New development is encouraged to use the community fork, which
includes backwards incompatible changes and fixes.
https://www.manim.community/

This presentation covers the community fork.

Implications: don't copy Manim code from Grant's videos directly and expect it
to work. It will require minor fixes. Don't copy/paste StackOverflow answers
without checking which fork the answer applies to (answerers may be confused
about this). It is currently not recommended to use general purpose LLMs trained
on "the internet" for answering `manim` coding questions. Better to use LLMs
trained on community fork documentation and examples.

## Install

### Linux

```bash
    # Start with installing uv (new-school python package tool)
    # https://docs.astral.sh/uv/getting-started/installation/
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Start a uv project
    mkdir project
    cd project
    uv init

    # Make sure general dependencies are present
    sudo apt update
    sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev

    # Add manim
    uv add manim

    # Optional install of TeX for math formulas
    sudo apt install texlive-full
```

## Usage

Once `manim` is installed, you have a Python package you can `import`
from Python code. You also have the `manim` command line tool.

Example code in file `examples.py`:

```py
    from manim import *

    class CreateCircle(Scene):
        def construct(self):
            circle = Circle()  # create a circle
            circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
            self.play(Create(circle))  # show the circle on screen
```

To see what it does:

```bash
    manim render -pql examples.py CreateCircle
```

This runs the example code and renders to a `.mp4` file, then
previews the video in a new window.

```
    -p      Preview the rendered video
    -ql     Choose low resolution quality
```

Quality levels:
```
    -ql     854x480 15FPS
    -qm     1280x720 30FPS
    -qh     1920x1080 60FPS
    -qp     2560x1440 60FPS
    -qk     3840x2160 60FPS
```

Usually the lowest quality level is fastest to render for development and is
good enough to see what is happening. For presenting slides, medium quality is
often adequate because of projector limitations. For publishing to YouTube high
quality or higher is recommended.

The output file is stored in a location like
`media/videos/<filename>/<resolution>/<class>.mp4`

## Concepts

Docs link: https://docs.manim.community/en/stable/index.html

In your Python code, a `Scene` object represents an animated video. Within the
`Scene` object there is a `construct()` method. Inside this method you create
objects to display, add them to the `Scene`, and animate them.

Your Python code can define more than one class that inherits from `Scene`. You
then can choose to render one or more of them from the command line `manim`.

## Some Manim Limitations

One thing `manim` doesn't do is compose multiple rendered animations into one
video. If you have something like a talking head video of yourself explaining a
concept and a `manim` animation of the concept, you probably want to use some
sort of traditional video editor to merge both videos together. You might put
the talking head in a corner of the concept animation, or cross-fade between a
full screen talking head to the concept animation and back again.

If you have background audio you want to integrate into a `manim` animation
(e.g. explanations) the easiest thing is to use a video editor and splice
together the audio and video and adjusting the timings to get things to match up
correctly.

If you are trying to fit a concept animation to an existing voice audio
explanation, it is possible to add delays and timing to the `manim` python
script but this can get tedious. There is no built-in graphical way to adjust
timing.










## Voiceovers

You can also use a tool in `manim` to generate/record voiceovers. The idea is
you write text to say, put it in your scene. Then the voiceover plugin calls
different TTS systems to generate artificial voice of your text. Once things are
stable, you can use a command line flag to record your own voice and use it
instead of the synthesized one.

https://voiceover.manim.community/en/latest/quickstart.html

## Other ideas

There are lots of JavaScript libraries for making animations, many are
spiritually an evolution of Flash. They often have a mix of programmatic
animation and graphical animation editors.

https://motioncanvas.io/ 

