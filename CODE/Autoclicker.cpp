#include <iostream>
#include <windows.h>
 
// Set default state to false
bool bState{ false };
 
void menu(bool bState)
{
	// Clears and prints to the console
	system("cls");
 
	std::cout << "GorillaX' autoclicker v1.0\n";
 
	if (bState)
	{
		std::cout << "Status: ON\n";
	}
	else
	{
		std::cout << "Status: OFF\n";
	}
}
 
int main()
{
	menu(bState);
	while (true)
	{
		// Check if 'X' is pressed
		if (GetAsyncKeyState(0x58) & 1)
		{
			// Switch bState value
			bState = !bState;
			// Print menu to console
			menu(bState);
		}
 
		if (bState)
		{
			// Simulate mouse click
			mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
		}
		Sleep(10);
	}
}