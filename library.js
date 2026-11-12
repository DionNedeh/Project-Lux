'use strict';
(() => {
  const list = document.querySelector('.catalogue-list');
  if (!list) return;
  const rows = [...list.querySelectorAll('.catalogue-row')];
  const search = document.querySelector('#catalogue-search');
  const topic = document.querySelector('#topic-filter');
  const order = document.querySelector('#sort-order');
  const buttons = [...document.querySelectorAll('[data-kind]')];
  const count = document.querySelector('#catalogue-count');
  const empty = document.querySelector('.catalogue-empty');
  const params = new URLSearchParams(location.search);
  const normalise = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  const data = window.LUX_LIBRARY || {};
  const haystacks = new Map(rows.map(row => [row, normalise(`${row.textContent} ${row.dataset.topics} ${data[row.dataset.slug]?.text || ''}`)]));
  let kind = buttons.some(button => button.dataset.kind === params.get('type')) ? params.get('type') : 'all';
  search.value = params.get('q') || '';
  if ([...topic.options].some(option => option.value === params.get('topic'))) topic.value = params.get('topic');
  if (params.get('sort') === 'updated') order.value = 'updated';
  function applyFilters(updateAddress = true) {
    const terms = [...normalise(search.value).matchAll(/"([^"]+)"|(\S+)/g)].map(match => match[1] || match[2]);
    let visible = 0;
    rows.forEach(row => {
      const match = (kind === 'all' || row.dataset.type === kind)
        && (topic.value === 'all' || row.dataset.topics.split(' ').includes(topic.value))
        && terms.every(term => haystacks.get(row).includes(term));
      row.hidden = !match;
      if (match) visible++;
    });
    const sorted = [...rows].sort((a, b) => {
      if (order.value === 'updated') {
        const diff = b.dataset.updated.localeCompare(a.dataset.updated);
        if (diff) return diff;
      }
      return (data[a.dataset.slug]?.title || a.textContent).localeCompare(data[b.dataset.slug]?.title || b.textContent, 'en');
    });
    list.append(...sorted);
    count.textContent = `${visible} of ${rows.length} research notes`;
    empty.hidden = visible > 0;
    buttons.forEach(button => {
      const selected = button.dataset.kind === kind;
      button.setAttribute('aria-pressed', String(selected));
      button.classList.toggle('active', selected);
    });
    if (updateAddress) {
      const next = new URLSearchParams();
      if (search.value.trim()) next.set('q', search.value.trim());
      if (kind !== 'all') next.set('type', kind);
      if (topic.value !== 'all') next.set('topic', topic.value);
      if (order.value !== 'title') next.set('sort', order.value);
      const query = next.toString();
      history.replaceState(null, '', location.pathname + (query ? `?${query}` : '') + location.hash);
    }
  }
  search.addEventListener('input', () => applyFilters());
  topic.addEventListener('change', () => applyFilters());
  order.addEventListener('change', () => applyFilters());
  buttons.forEach(button => button.addEventListener('click', () => { kind = button.dataset.kind; applyFilters(); }));
  document.querySelectorAll('.clear-filters').forEach(button => button.addEventListener('click', () => {
    kind = 'all'; search.value = ''; topic.value = 'all'; order.value = 'title'; applyFilters(); search.focus();
  }));
  document.querySelector('.catalogue-controls').hidden = false;
  applyFilters(false);
})();
