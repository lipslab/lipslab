From the original repository:

> A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

> I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

> ### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 
More detailed instructions can be found at https://academicpages.github.io/.


This is a repository of [LIPS LAB web site](https://lipslab.github.io/). Further you will find information for how to add content to the website (for maintainers).

# Instructions

## Important Locations
There are several main section of the website that correspond to several locations in the repository. 
1. [About](https://github.com/lipslab/lipslab.github.io/blob/master/_pages/about.md)
2. [Publications](https://github.com/lipslab/lipslab.github.io/tree/master/_publications)
3. [Projects](https://github.com/lipslab/lipslab.github.io/tree/master/_projects)
4. [Members](https://github.com/lipslab/lipslab.github.io/tree/master/_members)
5. [Vision](https://github.com/lipslab/lipslab.github.io/blob/master/_pages/vision.md)
6. [Contact](https://github.com/lipslab/lipslab.github.io/blob/master/_pages/contact.md)
7. [Images](https://github.com/lipslab/lipslab.github.io/tree/master/images)

## How to edit 

The editing is done using Markdown. Most basic information about markdown format can be found [here](https://www.markdownguide.org/basic-syntax/).  To edit a section, for example *[About](https://github.com/lipslab/lipslab.github.io/blob/master/_pages/about.md)*, press a edit button as shown on the image below.

![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_edit.png)

The editing process consists of filling in the forms and adding content after the main form.

![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_editing.png)

### Editing publications, members, and projects

These sections are generated automatically from several files. Take [publications](https://github.com/lipslab/lipslab.github.io/tree/master/_publications) for example. Each file corresponds to one bibliography item. In case many publications need to be added, there si a script to create neccessary files automatically from `bib` file. 

The example of a publication form is shown in the image below. The files for publications are read and used to generate the *Publications* section.

<p align="center">
<img src="https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_edit_publication.png" width="300"><img src="https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_publications_preview.png" width="300">
</p>

Similar forms can be found for adding projects ...
![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_edit_project.png)

and members.
![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_edit_member.png)

The form for members allows to add CV for each lab participant.

### Upload images

Use the folder `images` to upload neccessary figures. 
![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_upload.png)
![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_drop.png)

### Commit changes

After making changes to files, commit the final version 
![](https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/readme/readme_commit.png)
