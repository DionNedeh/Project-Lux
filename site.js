'use strict';
document.documentElement.classList.add('js');
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
