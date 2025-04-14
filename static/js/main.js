function scrollToSection(sectionId) {
    const section = document.getElementById(`section-${sectionId}`);
    section.scrollIntoView({ behavior: 'smooth' });
}

document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.section');
    const dotsContainer = document.querySelector('.navigation-dots');
    
    // Генерация точек
    sections.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.className = 'dot';
        dot.dataset.section = index + 1;
        dot.addEventListener('click', () => scrollToSection(index + 1));
        dotsContainer.appendChild(dot);
    });

    // Логика обновления активной точки
    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY + (window.innerHeight / 2);
        
        sections.forEach((section, index) => {
            const top = section.offsetTop;
            const bottom = top + section.offsetHeight;
            const dot = dotsContainer.children[index];
            
            if(scrollPosition >= top && scrollPosition <= bottom) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    });
});
