'use strict';
document.documentElement.classList.add('js');

// Advect the wire grid around the original torus. The projection never moves.
const fieldScene = document.querySelector('.plasma-scene');
const motionToggle = document.querySelector('.motion-toggle');
if (fieldScene && motionToggle) {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const canvas = document.createElement('canvas');
  canvas.className = 'field-grid-canvas';
  canvas.setAttribute('aria-hidden', 'true');
  const context = canvas.getContext('2d');
  if (context) {
    fieldScene.append(canvas);
    const samples = Array.from({length: 241}, (_, i) => {
      const u = Math.PI * 2 * i / 240;
      return [Math.cos(u), Math.sin(u), Math.cos(2 * u), Math.sin(2 * u)];
    });
    const rotationCos = Math.cos(-0.45);
    const rotationSin = Math.sin(-0.45);
    let phase = 0;
    let userPaused = false;
    let inView = false;
    let frame = 0;
    let lastPaint = 0;
    function drawGrid() {
      context.setTransform(canvas.width / 600, 0, 0, canvas.height / 540, 0, 0);
      context.clearRect(0, 0, 600, 540);
      context.lineWidth = 0.65;
      context.globalAlpha = 0.55;
      for (let j = 0; j < 64; j++) {
        const angle = Math.PI * 2 * j / 64 + phase;
        const cosPhase = Math.cos(angle);
        const sinPhase = Math.sin(angle);
        context.beginPath();
        samples.forEach(([cosU, sinU, cos2U, sin2U], i) => {
          const cosV = cosPhase * cos2U - sinPhase * sin2U;
          const sinV = sinPhase * cos2U + cosPhase * sin2U;
          const radius = 157 + 58 * cosV;
          const x = radius * cosU;
          const y = radius * sinU * 0.64 + 58 * sinV * 0.72;
          const px = 300 + x * rotationCos - y * rotationSin;
          const py = 268 + x * rotationSin + y * rotationCos;
          if (i === 0) context.moveTo(px, py); else context.lineTo(px, py);
        });
        context.strokeStyle = j % 3 ? '#a75b35' : '#c48d45';
        context.stroke();
      }
    }
    function resizeGrid() {
      const rect = fieldScene.getBoundingClientRect();
      const density = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, Math.round(rect.width * density));
      canvas.height = Math.max(1, Math.round(rect.height * density));
      drawGrid();
    }
    function animateGrid(now) {
      const elapsed = now - lastPaint;
      if (elapsed >= 1000 / 30) {
        phase = (phase + Math.min(elapsed, 100) * 0.00022) % (2 * Math.PI);
        lastPaint = now;
        drawGrid();
      }
      frame = requestAnimationFrame(animateGrid);
    }
    function updateFieldMotion() {
      const running = !userPaused && !reducedMotion.matches && inView && !document.hidden;
      fieldScene.classList.toggle('motion-ready', !reducedMotion.matches);
      fieldScene.classList.toggle('motion-running', running);
      if (running && !frame) {
        lastPaint = performance.now();
        frame = requestAnimationFrame(animateGrid);
      } else if (!running && frame) {
        cancelAnimationFrame(frame);
        frame = 0;
      }
      motionToggle.disabled = reducedMotion.matches;
      motionToggle.textContent = reducedMotion.matches ? 'Reduced motion enabled' : userPaused ? 'Play motion' : 'Pause motion';
    }
    resizeGrid();
    new ResizeObserver(resizeGrid).observe(fieldScene);
    motionToggle.hidden = false;
    motionToggle.addEventListener('click', () => { userPaused = !userPaused; updateFieldMotion(); });
    reducedMotion.addEventListener('change', updateFieldMotion);
    document.addEventListener('visibilitychange', updateFieldMotion);
    new IntersectionObserver(entries => {
      inView = entries[0].isIntersecting;
      updateFieldMotion();
    }, {threshold: 0}).observe(fieldScene);
    updateFieldMotion();
  }
}
const stageButtons = [...document.querySelectorAll('[data-stage]')];
const stagePanels = [...document.querySelectorAll('.stage-panel')];
function showStage(name) {
  stagePanels.forEach(panel => { panel.hidden = panel.id !== `stage-${name}`; });
  stageButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.stage === name)));
}
if (stageButtons.length) {
  document.querySelector('.stage-buttons').hidden = false;
  function followStageLink() {
    const stage = location.hash.replace('#stage-', '');
    if (['learn', 'predict', 'control'].includes(stage)) {
      showStage(stage);
      requestAnimationFrame(() => document.getElementById(`stage-${stage}`).scrollIntoView());
    }
  }
  showStage('learn');
  followStageLink();
  window.addEventListener('hashchange', followStageLink);
  stageButtons.forEach(button => button.addEventListener('click', () => showStage(button.dataset.stage)));
}
const rows = [...document.querySelectorAll('.library-section .library-row')];
const search = document.querySelector('#library-search');
const filters = [...document.querySelectorAll('[data-filter]')];
let selectedFilter = 'all';
function filterLibrary() {
  const terms = search.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  let shown = 0;
  rows.forEach(row => {
    const haystack = `${row.textContent} ${row.dataset.keywords || ''}`.toLocaleLowerCase();
    const matches = (selectedFilter === 'all' || row.dataset.category === selectedFilter) && terms.every(term => haystack.includes(term));
    row.hidden = !matches;
    if (matches) shown += 1;
  });
  document.querySelector('#result-count').textContent = `${shown} of ${rows.length} references`;
  document.querySelector('.empty-state').hidden = shown > 0;
  filters.forEach(button => {
    const active = button.dataset.filter === selectedFilter;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
}
if (search) {
  document.querySelector('.library-tools').hidden = false;
  search.addEventListener('input', filterLibrary);
  filters.forEach(button => button.addEventListener('click', () => { selectedFilter = button.dataset.filter; filterLibrary(); }));
  document.querySelector('#reset-search').addEventListener('click', () => { selectedFilter = 'all'; search.value = ''; filterLibrary(); search.focus(); });
}
