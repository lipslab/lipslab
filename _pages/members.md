---
layout: archive
title: "Members"
permalink: /members/
author_profile: false
gallery:
  - url: https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/3953273590_704e3899d5_m.jpg
    image_path: https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/3953273590_704e3899d5_m.jpg
    alt: "placeholder image 1"
    title: "Image 1 title caption"
  - url: https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/bio-photo-2.jpg
    image_path: https://raw.githubusercontent.com/lipslab/lipslab.github.io/master/images/bio-photo-2.jpg
    alt: "placeholder image 2"
    title: "Image 2 title caption"
---

{% include base_path %}

<div class="grid__wrapper">
  {% for member in site.members %}
    {% include archive-member.html type="grid" %}
  {% endfor %}
</div>

<!-- <div>
  {% include gallery caption="This is a sample gallery with **Markdown support**." %}
</div> -->