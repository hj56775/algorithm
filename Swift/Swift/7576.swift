//
//  7576.swift
//  PSSwift
//
//  Created by 유한준 on 2021/12/11.
//

import Foundation

func Q7576() {
    
    class Deque<T> {
        var enqueue: [T]
        var dequeue: [T] = []
        var count: Int {
            return enqueue.count + dequeue.count
        }
        var isEmpty: Bool {
            return enqueue.isEmpty && dequeue.isEmpty
        }
        var first: T? {
            if dequeue.isEmpty {
                return enqueue.first
            }
            return dequeue.last
        }
        
        init(_ queue: [T]) {
            enqueue = queue
        }
        
        func pushFirst(_ n: T) {
            dequeue.append(n)
        }
        
        func pushLast(_ n: T) {
            enqueue.append(n)
        }
        
        func popFirst() -> T? {
            if dequeue.isEmpty {
                dequeue = enqueue.reversed()
                enqueue.removeAll()
            }
            return dequeue.popLast()
        }
        
        func popLast() -> T? {
            var returnValue: T?
            if enqueue.isEmpty {
                dequeue.reverse()
                returnValue = dequeue.popLast()
                dequeue.reverse()
            } else {
                returnValue = enqueue.popLast()
            }
            return returnValue
        }
        
//        func contains(_ n: T) -> Bool {
//            return enqueue.contains(where: {$0 == n}) || dequeue.contains(where: {$0 == n})
//        }
        
        func removeAll() {
            enqueue.removeAll()
            dequeue.removeAll()
        }
    }
    
    let nAndM = readLine()!.split(separator: " ").map{ Int($0)! }
    let n = nAndM[0] // 가로
    let m = nAndM[1] // 세로
    
    var queue = [(Int, Int, Int)]()
    var deque = Deque(queue)
    var visited = [[Bool]](repeating: [Bool](repeating: false, count: n), count: m)
    var box = [[Int]]()
    let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    var goal = 0
    
    for i in 0..<m {
        let line = readLine()!.split(separator: " ").map{ Int($0)! }
        box.append(line)
        
        for j in 0..<n {
            if line[j] == 1 {
                deque.pushLast((i, j, 0))
            }
            else if line[j] == 0 {
                goal += 1
            }
        }
    }
    
    var result = 0
    var changed = 0
    
    func bfs() {
        while !deque.isEmpty {
//            let poped = queue.removeFirst()
            let poped = deque.popFirst()!
            let x = poped.0
            let y = poped.1
            let time = poped.2
            visited[x][y] = true
            
            for dir in dirs {
                let nx = x + dir.0
                let ny = y + dir.1
                
                if 0..<m ~= nx, 0..<n ~= ny, visited[nx][ny] == false, box[nx][ny] == 0 {
                    box[nx][ny] = 1
                    deque.pushLast((nx,ny, time + 1))
                    changed += 1
                    result = time + 1
                }
            }
        }
    }
    
    bfs()
    
    if changed == goal {
        print(result)
    } else {
        print(-1)
    }
}
