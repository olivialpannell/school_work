#include "graph.h"
#include <math.h>


// This function initializes an adjacency list for
// a graph.
// 
// Note that adj list is an array of """adj_node_t*""" which is passed
// in by reference.
// That is, you are passing in a pointer (i.e, *) to an array (i.e., *)
// of adj_node_t*, which is why list is of type adj_node_t***
void init_adj_list(adj_node_t ***list, int rows)
{
    //allocate memory and set it all equal to NULL
    *list = (adj_node_t **)malloc(sizeof(adj_node_t *) * rows);
    for (int i = 0; i < rows; i++) 
    {
        (*list)[i] = NULL;
    }
}


// This function creates a new adj_node_t node
// and initializes it with node->vid = vid
// and node->next = NULL;
// The function then returns this node
adj_node_t *create_node(int vid)
{
    //create a new node
    adj_node_t *newnode = (adj_node_t*)malloc(sizeof(adj_node_t));
    newnode->vid = vid;
    newnode->next = NULL;
    return newnode;
}


// Pass in the list and the row to which you need to add a new node
// First check that the adjacency list for the current row is not
// empty (i.e., NULL). If it is NULL, it is the first adjacent node.
// Otherwise, traverse the list until you reach the end, and then add
// the new node
void add_node(adj_node_t** list, int row, adj_node_t* node)
{
    //Create a temp
    adj_node_t *temp = list[row];
    //while not empty
    if(temp != NULL)
    {
        //get to the end of temp
        for (; temp->next != NULL; temp = temp->next);
        temp->next = node;
    }
    //if empty
    else
    {
        list[row] = node;
    }
}

// deqeueu a node from a queue
// and return the vertex id of the first member
// when list returns, it points to the next member in the queue
int remove_node(adj_node_t **list)
{
    //create temp node to keep values in
    //save vid into id and return it
    //then free temp
    adj_node_t *temp = *list;
    int id = temp->vid;
    *list = temp->next;
    free(temp);
    return id;
}


// This function constructs an adjacency list for a graph.
//
// adj_mat is a 2D array that represents the adjacency matrix
//
// list is passed in by reference from the main function so that
// it can be malloc'd via the init_adj_list function (see aobve)
//
// After initializing it go through each row and add its adjacent 
// nodes
void construct_adj_list(int **adj_mat, int rows, int cols, adj_node_t ***list)
{
    // verify that the adj matrix is correct
    if(rows != cols) {
        printf("Adjacency matrix is not square\n");
        exit(EXIT_FAILURE);
    }

    init_adj_list(list, rows);
    
    //create the adj list
    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < cols; j++)
        {
            //if there's a one in the adj matrix then use create with vid j
            //and add node with row i
            if(adj_mat[i][j] == 1)
            {
                adj_node_t *newnode = create_node(j);
                add_node(*list, i, newnode);           
            }
        }
    }
}

// This takes in an adjacency ilst and prints out the list
void print_adj_list(adj_node_t **list, int rows)
{
    assert(list);

    printf("---- Print Adj. List ----\n");
    for(int i = 0; i < rows; i++) {
        printf("|%d| -> ", i);
        adj_node_t* next = list[i];
        while(next != NULL) {
            printf("%d -> ", next->vid);
            next = next->next;
        }
        printf("END\n");
    }
    printf("--------\n\n");
}

void free_adj_list(adj_node_t **list, int rows)
{
    // free the list
    // for each row and until the end of the list
    for(int i = 0; i < rows; i++) 
    {
        adj_node_t *newnode = list[i];
        adj_node_t *temp;
        while(newnode != NULL)
        {
            temp = newnode->next;
            free(newnode);
            newnode = temp;
        }
    }
    //free the final list
    free(list);
}

void print_bfs_result(int rows, int *color, int *distance, int *parent)
{
    assert(color);
    assert(distance);
    assert(parent);

    printf("---- Print BFS Result ----\n");
    printf("Vert\tCol\tDis\tParent\n");
    for(int i = 0; i < rows; i++) {
        printf("%d\t%d\t%d\t%d\n", i, color[i], distance[i], parent[i]);
    }
    printf("--------\n\n");
}


// Do BFS here, given the source node and the
// graph's adjacency list
int bfs(adj_node_t **list, int rows, int source,
        int *color, int *distance, int *parent)
{
    // Make sure the source is a valid vertex
    if(source >= rows) {
        printf("Invalid source vertex\n");
        return 0;
    }
    // Make sure the adjacency list is not empty
    if(list == NULL) {
        printf("There is nothing in the adjacency list\n");
        return 0;
    }
    // Make sure all these are properly allocated
    assert(color);
    assert(distance);
    assert(parent);

    // Part 5 - Fill in the rest of this function

    //initialize the arrays  
    for(int i = 0; i < rows; i++)
    {
        color[i] = 0;
        distance[i] = INFINITY;
        parent[i] = -1;
    }
    //intialize the source
    color[source] = 1;
    distance[source] = 0;
    parent[source] = -1;

    //create Q
    adj_node_t *Q = create_node(source);
    adj_node_t *node = Q;
    while(Q != NULL)
    {
        int current = remove_node(&Q);
        for(adj_node_t *newnode = list[current]; newnode != NULL; newnode = newnode->next)
        {
            //add if not already visited
            if(color[newnode->vid] == 0)
            {
                color[newnode->vid] = 1;
                parent[newnode->vid] = current;
                //update distance
                if(distance[newnode->vid] > (distance[current] + 1))
                {
                    distance[newnode->vid] = distance[current] + 1;
                }
                adj_node_t *anothernode = create_node(newnode->vid);
                if(Q != NULL)
                {
                    node->next = anothernode;
                    node = node->next;
                }
                else{
                    Q = anothernode;
                    node = Q;
                }
            }
        }
    }

    #if DEBUG
    print_bfs_result(rows, color, distance, parent);
    #endif

    return 0;
}






