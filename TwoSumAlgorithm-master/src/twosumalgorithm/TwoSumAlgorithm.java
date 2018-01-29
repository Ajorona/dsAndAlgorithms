package twosumalgorithm;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;


public class TwoSumAlgorithm {
   final static long LOWER_BOUND = -10000;
   final static long UPPER_BOUND = 10000;
   static HashMap inputMap = new HashMap();
   static HashMap outputMap = new HashMap();
   static long x, y, t, value;
   static int count = 0;
   
   
   public static void main(String args[]) throws FileNotFoundException {

       makeInputHash();
       twoSum();
   }
   
   private static void makeInputHash() throws FileNotFoundException {
      Scanner input = new Scanner(new File("./input.txt"));
      while(input.hasNextLong()) {
          value = input.nextLong();
          inputMap.put(value, value);
      }
      input.close();
      System.out.println("input hash table constructed \n\n");
   }

    private static void twoSum() {
        Set<Long> keys = inputMap.keySet();
        for(Long key : keys) {
            twoSumCore(key);
        }       
    }           
           
    private static void twoSumCore(long x) {          
        for(long t = LOWER_BOUND; t <= UPPER_BOUND; t++) {
          y = t - x;
          if (inputMap.containsKey(y)){
              outputMap.put(t, t);
              System.out.println(outputMap.size());
          }     
        } 
    }
}
