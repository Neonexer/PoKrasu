document.addEventListener('DOMContentLoaded', () => {
    const showMoreLink = document.querySelector('.show-more');
    const moreCuisines = document.querySelectorAll('.more-cuisines');
  
    showMoreLink.addEventListener('click', (event) => {
      event.preventDefault();
      moreCuisines.forEach(cuisine => {
        cuisine.classList.toggle('hidden');
      });
  
      showMoreLink.textContent = moreCuisines[0].classList.contains('hidden') ? 'Показать больше' : 'Скрыть';
    });
  });
  