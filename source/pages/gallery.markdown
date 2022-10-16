---
layout: home
title: Gallery

gallery: true
---

<main markdown="1">

  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h1 class="fw-light">BruinBots Gallery</h1>
        <p class="lead text-muted">Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don’t simply skip over it entirely.</p>
      </div>
    </div>
  </section>

  <div class="album pb-5 bg-light">
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      {% for image in site.static_files %}
        {% if image.path contains 'assets/gallery' %}
            <div class="col">
              <div class="card shadow-sm">
                <img src="{{ image.path }}">
                <!-- <div class="card-body">
                  <p class="card-text"></p>
                  <div class="d-flex justify-content-between align-items-center">
                  </div>
                </div> -->
              </div>
            </div>
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>

</main>