#include "lists.h"

/**
 * check_cycle - identifies if a linked list contains a cycle
 * @list: pointer to the head node of the linked list
 * 
 * Description: Uses Floyd's Tortoise and Hare algorithm to
 * efficiently detect cycles without extra memory usage
 * used slow and fast as a variable
 * 
 * Return: 1 if cycle exists, 0 otherwise
 */
int check_cycle(listint_t *list);
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
        return (0);
	
	while (fast && fast->next)
	{
		
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
            return (1);
	}
	
	return (0);
}
