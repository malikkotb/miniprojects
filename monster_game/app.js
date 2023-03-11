function getRandomVal(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

const app = Vue.createApp({
    data() {
        return {
            playerHealth: 100,
            monsterHealth: 100,
            currentround: 0,
            winner: null,
            logMessages: [],
        };
    },
    computed: {
        monsterBarStyles() {
            if (this.monsterHealth < 0) {
                return {width: '0%'};
            }
            return {width: this.monsterHealth + '%'};
        },
        playerBarStyles() {
            if (this.playerHealth < 0) {
                return {width: '0%'};
            }
            return {width: this.playerHealth + '%'};
        },
        specialAttackAvailable() {
            return this.currentround % 3 !== 0
        }
    },
    watch: { // use watchers to determine winner/loser
        playerHealth(value) {
            if (value <= 0 && this.monsterHealth <= 0) {
                // draw
                this.winner = 'draw';
            } else if (value <= 0) {
                // player lost
                this.winner = 'monster';
            }
        },
        monsterHealth(value) { // value refers to the value of monsterHealth data attribute
            if (value <= 0 && this.playerHealth <= 0) {
                // draw
                this.winner = 'draw';
            } else if (value <= 0) {
                // monster lost
                this.winner = 'player';
            }
        },
    },
    methods: {
        startGame() {
            // just reset parameters
            this.playerHealth = 100;
            this.monsterHealth = 100;
            this.currentround = 0;
            this.winner = null;
            this.logMessages = [];
        },
        attackMonster() {
            this.currentround++;
            const attackVal = getRandomVal(5, 12);
            this.monsterHealth -= attackVal;
            this.addLogMessage('player', 'attack', attackVal);
            this.attackPlayer();
        },
        attackPlayer() {
            const attackVal = getRandomVal(8, 15);
            this.playerHealth -= attackVal;
            this.addLogMessage('monster', 'attack', attackVal);
        },
        specialAttackMonster() {
            this.currentround++;
            const attackVal = getRandomVal(10, 25);
            this.monsterHealth -= attackVal;
            this.addLogMessage('player', 'attack', attackVal);
            this.attackPlayer();
        },
        healPlayer() {
            this.currentround++;
            const healVal = getRandomVal(8, 20);
            if (this.playerHealth + healVal > 100) {
                this.playerHealth = 100;
            } else {
                this.playerHealth += healVal;
            }
            this.addLogMessage('player', 'heal', healVal);
            this.attackPlayer();
        },
        surrender() {
            this.winner = 'monster';
        },
        addLogMessage(who, what, value) { // value: how much damage was dealt
            // latest message should always be on top 
            this.logMessages.unshift({
                actionBy: who,
                actionType: what,
                actionValue: value,
            }); // unshift adds to beginning of array
            

        }
    },
});

app.mount('#game');