package MM;

import java.util.ArrayList;

public class MaxHeap
{
   public static ArrayList<Integer> buildMaxHeap(ArrayList<Integer> arr)
   {
      int heapSize = arr.size();
      for(int i = (heapSize/2) - 1; i >= 0; i--) {
         maxHeapify(arr, i);
      }
      return arr;
   }
   private static void maxHeapify(ArrayList<Integer> arr, int i)
   {
      int heapSize, largestIndex, largestValue, parent, l, lChild, r, rChild;
      
      heapSize = arr.size();
      l = getLeft(i);
      r = getRight(i);
      parent = arr.get(i);
      largestIndex = i;
      largestValue = arr.get(i);
      
      if (l < heapSize) {
          lChild = arr.get(l);
          if (lChild > parent) {
            largestIndex = l;
            largestValue = arr.get(largestIndex);
        } 
      }

      if (r < heapSize) {
          rChild = arr.get(r);
          if (rChild > largestValue) {
              largestIndex = r;
              largestValue = arr.get(largestIndex);
          }
      }
      if (largestIndex != i) {
         arr.set(largestIndex, parent);
         arr.set(i, largestValue);
         maxHeapify(arr, largestIndex);
      }
   }
   private static int getLeft(int i) {
      return (2*i + 1);
   }
   private static int getRight(int i) {
      
      return 2*(i+1);
   }
}

