---
layout: home
title: Gallery

gallery: true
---

<main markdown="1">

  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light bruinbots-title">BruinBots Gallery</h1>
        <p class="lead text-muted bruinbots-paragraph">This is the BruinBots Gallery for the most recent season.</p>
      </div>
    </div>
  </section>

  <div class="album pb-5 bg-light">
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-1 row-cols-md-2 g-3" style="width: 100%;">
      {% assign num = 0 %}
      {% for image in site.static_files %}
        {% if image.path contains 'assets/gallery' %}
            <div class="col">
              <div class="card shadow-sm">
                <a href="{{ image.path }}" target="_blank" class="card">
                  <img src="{{ image.path }}">
                </a>
              </div>
            </div>
           {% assign num = num | plus: 1 %}
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>

</main>