const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-navigation');
const mobile = window.matchMedia('(max-width: 1050px)');

function setMenu(open, returnFocus = false) {
  navigation.hidden = mobile.matches && !open;
  toggle.setAttribute('aria-expanded', String(mobile.matches && open));
  toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  toggle.querySelector('span').textContent = open ? 'Fermer' : 'Menu';
  if (returnFocus) toggle.focus();
}

toggle.hidden = false;
document.documentElement.classList.add('js');
setMenu(false);
toggle.addEventListener('click', () => {
  setMenu(toggle.getAttribute('aria-expanded') !== 'true');
});
navigation.addEventListener('click', event => {
  const link = event.target.closest('a');
  if (mobile.matches && link) {
    setMenu(false);
    const section = document.querySelector(link.getAttribute('href'));
    if (section) {
      section.setAttribute('tabindex', '-1');
      section.focus({ preventScroll: true });
    }
  }
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    setMenu(false, true);
  }
});
document.addEventListener('click', event => {
  if (mobile.matches && !navigation.contains(event.target) && !toggle.contains(event.target)) {
    setMenu(false);
  }
});
mobile.addEventListener('change', () => setMenu(false));
document.querySelector('[data-year]').textContent = String(new Date().getFullYear());
