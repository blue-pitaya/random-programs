#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define true 1
#define false 0
typedef int bool;

const int side_size = 9;
const int grid_size = 3;
const int size = side_size * side_size;

void clear_board(int* board) {
  for (int i = 0; i < size; i++) board[i] = 0;
}

void print_board(int* board) {
  for (int i = 0; i < size; i++) {
    printf("%d ", board[i]);
    if (i % side_size == (side_size - 1)) {
      printf("\n");
    }
  }
}

int flat_pos(int row, int col) {
  return row * side_size + col;
}

bool valid(int n, int row, int col, int* board) {
  const int n_position = flat_pos(row, col);
  int pos;

  // row check
  for (int i = 0; i < side_size; i++) {
    pos = flat_pos(row, i);
    if (pos != n_position && board[pos] == n) return false;
  }

  // col check
  for (int i = 0; i < side_size; i++) {
    pos = flat_pos(i, col);
    if (pos != n_position && board[pos] == n) return false;
  }

  // grid check
  const int grid_row = row / grid_size;
  const int grid_col = col / grid_size;
  const int row_from = grid_row * grid_size;
  const int row_to = row_from + grid_size;
  const int col_from = grid_col * grid_size;
  const int col_to = col_from + grid_size;

  for (int r = row_from; r < row_to; r++) {
    for (int c = col_from; c < col_to; c++) {
      pos = flat_pos(r, c);
      if (pos != n_position && board[pos] == n) return false;
    }
  }

  return true;
}

bool is_valid(int n, int pos, int* board) {
  valid(n, pos / side_size, pos % side_size, board);
}

int main() {
  srand(time(NULL));

  int board[size];
  int stack[size];
  int s_ptr = 0;

  clear_board(board);
  clear_board(stack);

  //MAIN
  const int max_iterations = 10000000;

  int iteration = 0;
  int current;
  while (iteration < max_iterations) {
    iteration++;
    stack[s_ptr]++;
    current = stack[s_ptr];

    if (current > side_size) {
      board[s_ptr] = 0;
      stack[s_ptr] = 0;
      s_ptr--;
      continue;
    }

    if (is_valid(current, s_ptr, board)) {
      board[s_ptr] = stack[s_ptr];
      s_ptr++;

      if (s_ptr >= size) break;
    } 
  }

  printf("Sudoku found on iteration: %d\n", iteration);
  print_board(board);

  return 0;
}
