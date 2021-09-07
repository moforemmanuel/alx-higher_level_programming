#include "lists.h"
/**
 * check_cycle - checks if there exists a cycle in a singly linked list
 * @list: singly linked list to be checked
 * Return: 0 if no cycle, 1 if cycle exists
 */

int check_cycle(listint_t *list)
{
  listint_t *present;

  if (!list)
    return (0);

  present = list->next;

  while (present != NULL)
    {
      if (present == list)
	return (1);
      present = present->next;
    }

  return (0);
}
