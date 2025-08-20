import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수

        for(int tc=1; tc<=T; tc++){
            String[] hw = br.readLine().split(" ");
            int h = Integer.parseInt(hw[0]);
            int w = Integer.parseInt(hw[1]);
            char[][] map = new char[h][w];

            int tankX = -1, tankY = -1;
            for(int i=0; i<h; i++){
                String line = br.readLine();
                for(int j=0; j<w; j++){
                    map[i][j] = line.charAt(j);
                    if(map[i][j] == '^' || map[i][j] == 'v' || map[i][j] == '<' || map[i][j] == '>'){
                        tankX = i;
                        tankY = j;
                    }
                }
            }

            int n = Integer.parseInt(br.readLine());
            String commands = br.readLine();

            for(char cmd : commands.toCharArray()){
                int x = tankX;
                int y = tankY;

                switch(cmd){
                    case 'U':
                        map[x][y] = '^';
                        if(x-1 >=0 && map[x-1][y]=='.'){
                            tankX = x-1;
                            map[tankX][y] = '^';
                            map[x][y] = '.';
                        }
                        break;
                    case 'D':
                        map[x][y] = 'v';
                        if(x+1 < h && map[x+1][y]=='.'){
                            tankX = x+1;
                            map[tankX][y] = 'v';
                            map[x][y] = '.';
                        }
                        break;
                    case 'L':
                        map[x][y] = '<';
                        if(y-1 >=0 && map[x][y-1]=='.'){
                            tankY = y-1;
                            map[x][tankY] = '<';
                            map[x][y] = '.';
                        }
                        break;
                    case 'R':
                        map[x][y] = '>';
                        if(y+1 < w && map[x][y+1]=='.'){
                            tankY = y+1;
                            map[x][tankY] = '>';
                            map[x][y] = '.';
                        }
                        break;
                    case 'S':
                        char dir = map[x][y];
                        int nx = x, ny = y;
                        if(dir=='^'){
                            for(int cx = x-1; cx >=0; cx--){
                                if(map[cx][y]=='*'){ map[cx][y]='.'; break; }
                                else if(map[cx][y]=='#') break;
                            }
                        } else if(dir=='v'){
                            for(int cx = x+1; cx < h; cx++){
                                if(map[cx][y]=='*'){ map[cx][y]='.'; break; }
                                else if(map[cx][y]=='#') break;
                            }
                        } else if(dir=='<'){
                            for(int cy = y-1; cy >=0; cy--){
                                if(map[x][cy]=='*'){ map[x][cy]='.'; break; }
                                else if(map[x][cy]=='#') break;
                            }
                        } else if(dir=='>'){
                            for(int cy = y+1; cy < w; cy++){
                                if(map[x][cy]=='*'){ map[x][cy]='.'; break; }
                                else if(map[x][cy]=='#') break;
                            }
                        }
                        break;
                }
            }

            // 출력
            System.out.print("#"+tc+" ");
            for(int i=0; i<h; i++){
                for(int j=0; j<w; j++){
                    System.out.print(map[i][j]);
                }
                System.out.println();
            }
        }
    }
}
