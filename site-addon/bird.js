/* Optional Easter egg: remove site-addon/ and its workflow step to disable it. */
(function () {
  "use strict";

  var bird = document.createElement("button");
  bird.id = "camat-bird-easter-egg";
  bird.type = "button";
  bird.textContent = "🐦";
  bird.title = "Ein kleiner musikalischer Gast";
  bird.setAttribute("aria-label", "Kleines Vöglein flattern lassen");
  document.body.appendChild(bird);

  function replay(className) {
    bird.classList.remove(className);
    void bird.offsetWidth;
    bird.classList.add(className);
    bird.addEventListener("animationend", function () {
      bird.classList.remove(className);
    }, { once: true });
  }

  bird.addEventListener("click", function () {
    replay("is-flapping");
  });

  function hopLater() {
    var delay = 4500 + Math.random() * 6500;
    window.setTimeout(function () {
      replay("is-hopping");
      hopLater();
    }, delay);
  }

  hopLater();
}());
