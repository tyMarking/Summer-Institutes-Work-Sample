/**
 * Declares a dictionary's functionality.
 */

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

struct node {
    struct node *children[27]; //mem fro 27
    //int numChilds = 0;
    char character;
    bool isEOW; //is end of word
};
typedef struct node node;

typedef struct unloadNode {
    node *node;
    struct unloadNode *unloadNode;
} unloadNode;
typedef struct unloadNode unlaodNode;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word);

bool checkRec(char *word, node *pNode);
/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary);

/**
 * Recursive method for creating nodes to represent chars of word
 */
void createNodes(char *word, node *pNode);


/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void);

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void);

void unloadNodes(node *node);

#endif // DICTIONARY_H
