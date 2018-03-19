$(function () {

  let width, height, canvas, ctx, circles, target, animateHeader = true;

  // Main
  initHeader();
  addListeners();

  function initHeader() {
    width = getClientWidth();
    height = getClientHeight();
    target = {x: 0, y: height};

    canvas = document.getElementById('canvas');

    canvas.width = width;
    canvas.height = height;
    canvas.style.backgroundImage = 'linear-gradient(200deg, #A1CEE1, #DBC691)';
    ctx = canvas.getContext('2d');

    // create particles
    circles = [];
    for (let x = 0; x < width * 0.5; x++) {
      circles.push(new Circle());
    }
    animate();
  }

  // Event handling
  function addListeners() {
    window.addEventListener('scroll', scrollCheck);
    window.addEventListener('resize', resize);
  }

  function scrollCheck() {
    animateHeader = document.body.scrollTop <= height;
  }

  function resize() {
    width = getClientWidth();
    height = getClientHeight();
    canvas.width = width;
    canvas.height = height;
  }

  function animate() {
    if (animateHeader) {
      ctx.clearRect(0, 0, width, height);
      for (let i in circles) {
        circles[i].draw();
      }
    }
    requestAnimationFrame(animate);
  }

  // Canvas manipulation
  function Circle() {
    let _this = this;

    // constructor
    (function () {
      _this.pos = {};
      init();
    })();

    function init() {
      _this.pos.x = Math.random() * width;
      _this.pos.y = height + Math.random() * 100;
      _this.alpha = 0.1 + Math.random() * 0.3;
      _this.scale = 0.1 + Math.random() * 0.3;
      _this.velocity = Math.random();
    }

    this.draw = function () {
      if (_this.alpha <= 0) {
        init();
      }
      _this.pos.y -= _this.velocity;
      _this.alpha -= 0.0005;
      ctx.beginPath();
      ctx.arc(_this.pos.x, _this.pos.y, _this.scale * 10, 0, 2 * Math.PI, false);
      ctx.fillStyle = 'rgba(255,255,255,' + _this.alpha + ')';
      // ctx.fillStyle = 'rgba(11,11,11,' + _this.alpha + ')';
      ctx.fill();
    };
  }
});

