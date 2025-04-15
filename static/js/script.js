document.getElementById('quiz-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let score = 0;
    const totalQuestions = questions.length;
    
    // Create an array of correct answers
    const correctAnswers = questions.map(question => question.correct);

    // Check answers
    for (let i = 0; i < totalQuestions; i++) {
        const selectedOption = document.querySelector(`input[name="question${i + 1}"]:checked`);
        if (selectedOption && selectedOption.value === correctAnswers[i]) {
            score++;
        }
    }
    
    const percentage = (score / totalQuestions) * 100;
    document.getElementById('score').innerText = percentage.toFixed(0);
    document.getElementById('result').classList.remove('hidden');
});
