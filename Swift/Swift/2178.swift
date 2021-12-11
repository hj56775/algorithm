//
//  2178.swift
//  PSSwift
//
//  Created by 유한준 on 2021/12/11.
//

import Foundation

func Q2178() {
    let nAndM = readLine()!.split(separator: " ").map{ Int($0)! }
    let n = nAndM[0]
    let m = nAndM[1]
    
    var maze = [[Int]]()
    var visited = [[Bool]](repeating: [Bool](repeating: false, count: m), count: n)
    var distance = [[Int]](repeating: [Int](repeating: 0, count: m), count: n)
    
    let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for _ in 0..<n {
        let row = Array(String(readLine()!)).map{ Int(String($0))! }
        maze.append(row)
    }
    
    var queue: [(Int,Int)] = [(0,0)]
    
    func bfs() {
        distance[0][0] = 1
        visited[0][0] = true
        
        while !queue.isEmpty {
            let poped = queue.removeFirst()
            
            let x = poped.0
            let y = poped.1
            
            for dir in dirs {
                let nx = x + dir.0
                let ny = y + dir.1
                
                if nx >= 0, nx < n, ny >= 0 , ny < m, maze[nx][ny] == 1,visited[nx][ny] == false {
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = true
                    queue.append((nx, ny))
                }
            }
        }
    }
    
    bfs()
    
    print(distance[n - 1][m - 1])
}
