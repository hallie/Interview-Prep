#include <iostream>

using namespace std;

struct nodeType {
	int item;
	nodeType *next;
};

class stackType {
	public:
		stackType();
		int getMaxLength();	   //returns max length of queue
		void setMaxLength(int ml); //Sets max length of queue
		bool isEmpty() const;	   //Checks to see if queue is empty
		bool isFull() const;	   //Checks to see if queue is full
		void enqueue(int q);	   //Adds an integer to queue
		int dequeue();		   //Removes last integer from queue
		void print();		   //Prints contents of queue
	private:
		nodeType *first;	//Pointer to first node
		nodeType *last;		//Pointer to last node
		int max_length;		//Maximum size of queue
		int length;		//Current size of queue
};

stackType::stackType() {
	first = NULL;			//Initializes first pointer to NULL
	last = NULL;			//Initializes last pointer to NULL
	length = 0;			//Initializes length to zero
	max_length = -1;
}

int stackType::getMaxLength() {
	return max_length;
}

void stackType::setMaxLength(int ml) {	//Sets max length of queue
	max_length = ml;
}

bool stackType::isEmpty() const {
	if (first == NULL) {
		return true;
	}
	else {
		return false;
	}
}

bool stackType::isFull() const {
	if (length == max_length) {
		return true;
	}
	else {
		return false;
	}
}

void stackType::enqueue(int q) {
	if (isEmpty()) {			//Case for user adding to empty queue
		first = new nodeType;
		first->item = q;
		first->next = NULL;
		last = first;
	}
	else {				        //Adds to the queue
		int i = 0;
		last->next = new nodeType;
		last = last->next;
		last->item = q;
		last->next = NULL;
	}
	length += 1;			        //Increments the length by one
}

int stackType::dequeue() {
	int d;					//Initializes a variable d
	d = last->item;				//Assigns contents of last to d
	if (first == last) {			//Handles case of queue being one long
		first = NULL;
		last = NULL;
	}
	else {					//Removes the last node from the queue
                nodeType *current;
                for (current = first; current->next != last; current = current->next);
		last = current;
		last->next = NULL;
	}
	length -= 1;				//Decrements the length by one
	return d;				//Returns the integer d
}

void stackType::print() {
    nodeType *current;
    int i;
    cout << "Your queue:\n";
	for(current = first; i++ < length; current = current->next) {
		cout << " | " << current->item << " | -->";
	}
	cout << endl;
}

int main() {
	stackType queue;
	bool done = false;
	char next;
	int ml;
	
	cout << "Welcome to the Queue!\n";
	
	cout << "What is the length of the queue? ";
	cin >> ml;
	queue.setMaxLength(ml);
	
	do {
		cout << "What would you like to do next?\n\t(a) Enqueue\n\t(b) Dequeue\n\t(c) Quit\n";
		cin >> next;
		if (next == 'a' || next == 'A') {
			if (!queue.isFull()) {		//Makes sure the queue isn't full before asking for an integer
				int i;
				cout << "Please enter and integer to add to the queue: ";
				cin >> i;
				queue.enqueue(i);
			}
			else {
				cout << "Sorry! The stack is full!\n";
			}
		}
		else if (next == 'b' || next == 'B') {
			if (!queue.isEmpty()) {		//Makes sure the queue isn't empty before trying to dequeue
				cout << "The removed integer is " << queue.dequeue() << endl;
			}
			else {
				cout << "O no! The stack is empty!\n";
			}
		}
		else if (next == 'c' || next == 'C') {
			cout << "Ok, then! Seeya!\n";
			if (!queue.isEmpty()) {		//Prints the contents of the queue if not empty
				queue.print();
			}
			done = true;			//Ends the prompting
		}
		else {					//Handles the case of the user inputting the wrong command
			cout << "Invalid command. Please try again!\n";
		}
	} while(!done);

	return 0;
}
