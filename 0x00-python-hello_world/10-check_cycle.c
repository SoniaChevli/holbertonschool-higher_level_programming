#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * check_cycle - checks to see if cycle in list
 *@list: linked list to check
 *
 *Return: 0 if no cycle. 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *temp2;

	temp = list;
	temp2 = list;

	while (temp != NULL && temp2 != NULL)
	{
		temp = temp->next;
		if (temp == NULL)
			return (0);
		temp = temp->next;
		temp2 = temp2->next;

		if (temp == temp2)
			return (1);
	}
	return (0);
}
