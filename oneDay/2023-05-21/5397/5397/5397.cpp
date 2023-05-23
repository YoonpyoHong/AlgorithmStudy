#include <iostream>
#include <string>

using namespace std;

typedef struct node {
	node* front;
	node* back;
	char value;
}node;

void findPassword() {
	node* root = (node*)calloc(1, sizeof(node));
	node* end = (node*)calloc(1, sizeof(node));
	node* current;
	root->front = NULL;
	root->back = end;
	end->front = root;
	end->back = NULL;
	current = root;
	string inputText;
	cin >> inputText;
	for (int i = 0; i < inputText.length(); i++) {
		if (inputText[i] == '<') {
			if (current->front != NULL) {
				current = current->front;
			}
		}
		else if (inputText[i] == '>') {
			if (current->back != end) {
				current = current->back;
			}
		}
		else if (inputText[i] == '-') {
			if (current != root) {
				node* target = current;
				current->front->back = current->back;
				current->back->front = current-> front;
				current = current->front;
				free(target);
			}
		}
		else {
			node* newNode = (node*)calloc(1, sizeof(node));
			newNode->back = current->back;
			current->back = newNode;
			newNode->back->front = newNode;
			newNode->front = current;
			newNode->value = inputText[i];
			current = newNode;
		}
	}
	node* printNode = root->back;
	while (printNode != end) {
		cout << printNode->value;
		printNode = printNode->back;
	}
	cout << "\n";
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		findPassword();
	}
}