---
layout: archive
title: "Members"
permalink: /members/
author_profile: true
---

{% include base_path %}

<div class="grid__wrapper">
  {% for member in site.members %}
    {% include archive-member.html type="grid" %}
  {% endfor %}
</div>
