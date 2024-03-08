function filterGames() {
    var filter = document.getElementById('searchInput').value.toUpperCase();
    var games = document.getElementsByClassName('game-grid')[0].getElementsByTagName('a');
  
    for (var i = 0; i < games.length; i++) {
      var gameTitle = games[i].getAttribute('onclick').split("'")[3].toUpperCase();
      if (gameTitle.indexOf(filter) > -1) {
        games[i].style.display = '';
      } else {
        games[i].style.display = 'none';
      }
    }
  }
  
