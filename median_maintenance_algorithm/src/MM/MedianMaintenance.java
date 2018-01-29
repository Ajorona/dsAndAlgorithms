package MM;


import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Stream;

public class MedianMaintenance {
    
    
    public static void main(String[] args) {
            double medianSum = 0;
            Stream<String> fileStream = null;
            ArrayList<Integer> highHeap, lowHeap, medianList;
            highHeap = new ArrayList<>();
            lowHeap = new ArrayList<>();
            medianList = new ArrayList<>();

            Path path = Paths.get("./input.txt");
            try (Stream<String> input = Files.lines(path)) {
                input.forEach(value -> placeValue(value, highHeap, lowHeap, medianList));
            } catch (IOException e) {
                e.printStackTrace();
                System.exit(0);
            }
            
            for(double i : medianList) {
                medianSum += i;
            }
            
            try {
                PrintWriter writer = new PrintWriter("output.txt", "UTF-8");    
                writer.println("lowHeap: " + Arrays.toString(lowHeap.toArray()));
                writer.println("highHeap: " + Arrays.toString(highHeap.toArray()));
                writer.format("median Sum Modulo 10000 is: %.4f%n", (medianSum % 10000));
                writer.close();
            } catch (IOException e) {
                e.printStackTrace();
                System.exit(0);
            }
            
        System.exit(0);
    }
	
    public static void placeValue(String elemString, ArrayList<Integer> highHeap,
                      ArrayList<Integer> lowHeap, ArrayList<Integer> medianList){

            int elem = Integer.parseInt(elemString);
            int primaryVal, lowMax, highMin, sizeHigh, sizeLow;
            
            //Initialize the low Heap and high Heap data structures.
            if (lowHeap.isEmpty() || highHeap.isEmpty()) {
                if (lowHeap.isEmpty() && highHeap.isEmpty()) {
                    highHeap.add(elem);
                    medianList.add(elem);
                    return;
                }
                primaryVal = highHeap.get(0);
                if (elem > primaryVal) {
                    lowHeap.set(0, primaryVal);
                    highHeap.set(0, elem);
                    medianList.add(primaryVal);
                    return;
                }
                else {
                    lowHeap.add(elem);
                    medianList.add(elem);
                    return;
                }
            }

            highMin = highHeap.get(0);
            lowMax = lowHeap.get(0);

            if (elem > highMin) {
                    highHeap.add(elem);
            }
            else if (elem < lowMax) {
                    lowHeap.add(elem);
            }
            else {
                    highHeap.add(elem);
            }
            
            sizeHigh = highHeap.size();
            sizeLow = lowHeap.size();

            //rebuild Heaps after addition of new elements
            MaxHeap.buildMaxHeap(lowHeap); 
            MinHeap.buildMinHeap(highHeap);

            /* balance the heap structures . .
             * NOTE: the abs difference does not exceed 1 if n is even,
             * The abs difference does not exceed 2 if n is odd.
             * Therefore no looping is necessasry (only 1 conditional)
            */
            if ((sizeHigh + sizeLow) % 2 == 0) {
                if (sizeHigh > sizeLow) {
                    lowHeap.add(highHeap.get(0));
                    highHeap.remove(0);                    
                }
                else if (sizeHigh < sizeLow) {
                    highHeap.add(lowHeap.get(0));
                    lowHeap.remove(0);
                }
            }
            else {
                if (Math.abs(sizeHigh - sizeLow) > 1) {
                    if (sizeHigh > sizeLow) {
                            lowHeap.add(highHeap.get(0));
                            highHeap.remove(0);
                    }
                    else {
                            highHeap.add(lowHeap.get(0));
                            lowHeap.remove(0);
                    }
                }
            }                        
            
            //re-build heap property before finding median . . 
            MaxHeap.buildMaxHeap(lowHeap); 
            MinHeap.buildMinHeap(highHeap);
            highMin = highHeap.get(0);
            lowMax = lowHeap.get(0);
            
            
            /* Test to get median at each step. . .
             * if odd, this is (n+1) / 2
             * if even, this is n / 2
            */
           
            if((sizeHigh + sizeLow) % 2 == 0) {
                if(highMin > lowMax) {
                    medianList.add(lowMax);
                }
                else {
                    medianList.add(highMin);
                }
            }
            else {
                if(sizeHigh > sizeLow) {
                    medianList.add(highMin);
                }
                else {
                    medianList.add(lowMax);
                }
            }
            return;
    }
}
