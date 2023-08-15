#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int quan, freq;
long long result;
priority_queue<long long, vector<long long>, greater<long long>> cards;

void input() {
	long long card;
	cin >> quan >> freq;
	for (int i = 0; i < quan; i++) {
		cin >> card;
		cards.push(card);
	}
}

void coalesce() {
	long long firstCard,secondCard, newCard;
	for (int i = 0; i < freq; i++) {
		firstCard = cards.top();
		cards.pop();
		secondCard = cards.top();
		cards.pop();
		newCard = firstCard + secondCard;
		cards.push(newCard);
		cards.push(newCard);
	}
}

void makeResult() {
	while (!cards.empty()) {
		result += cards.top();
		cards.pop();
	}
	cout << result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	input();
	coalesce();
	makeResult();

}