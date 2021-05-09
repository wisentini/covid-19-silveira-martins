async function getData(api_url) {
  const response = await fetch(api_url);
  const data = await response.json();

  return data;
}

function createHTMLCards(titles, numbers, updates) {
  const entries_length = titles.length;
  let htmlCards = [];

  for (let i = 0; i < entries_length; i++) {
    htmlCards.push(`
    <div class="card">
        <span class="card-number">${numbers[i]}</span>
        <span class="card-title">${titles[i]}</span>
        <hr>
        <div class="card-update">
            <span class="card-update-text">NOVOS ${titles[i].toUpperCase()}:</span>
            <span class="card-update-number">${updates[i]}</span>
        </div>
    </div>
    `);
  }

  return htmlCards;
}

(async () => {
  const titles = await getData('https://covid-19-silveira-martins.herokuapp.com/titles');
  const numbers = await getData('https://covid-19-silveira-martins.herokuapp.com/numbers');
  const updates = await getData('https://covid-19-silveira-martins.herokuapp.com/updates');
  const lastUpdatedDate = await getData('https://covid-19-silveira-martins.herokuapp.com/last-updated-date');
  const htmlCards = createHTMLCards(titles, numbers, updates).join('');

  document.querySelector('.last-updated-date').innerHTML += `<span class="section-update-date">Atualizado na ${lastUpdatedDate}</span>`;
  document.querySelector('.main').innerHTML = htmlCards;
})();
