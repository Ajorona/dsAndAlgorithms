package MM;

import java.util.ArrayList;


public class MinHeap
{
   public static ArrayList<Integer> buildMinHeap(ArrayList<Integer> arr)
   {
      int heapSize = arr.size();
      for(int i = (heapSize/2) - 1; i >= 0; i--) {
         minHeapify(arr, i);
      }
      return arr;
   }
   private static void minHeapify(ArrayList<Integer> arr, int i)
   {
	  int heapSize, smallestIndex, smallestValue, parent, l, lChild, r, rChild;
          
      heapSize = arr.size();
      l = getLeft(i);
      r = getRight(i);
      parent = arr.get(i);
      smallestIndex = i;
      smallestValue = arr.get(i);

      if (l < heapSize) {
        lChild = arr.get(l);
        if (lChild < parent) {
            smallestIndex = l;
            smallestValue = arr.get(smallestIndex);
        }
      }
      
      if (r < heapSize) {
          rChild = arr.get(r);
          if(rChild < smallestValue) {
            smallestIndex = r;
            smallestValue = arr.get(smallestIndex);
          }
      }
      if (smallestIndex != i) {
         arr.set(smallestIndex, parent);
         arr.set(i, smallestValue);
         minHeapify(arr, smallestIndex);
      }
   }

   private static int getLeft(int i) {
      return (2*i + 1);
   }
   private static int getRight(int i) {
      return 2*(i+1);
   }
}
