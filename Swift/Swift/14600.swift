//
//  14600.swift
//  Swift
//
//  Created by 유한준 on 2021/10/03.
//

import Foundation

func Q14600() {
    let k = Int(readLine()!)!
    let position = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let length = Int(pow(2, Float(k)))
    let row = [Int](repeating: 0, count: length)
    var map = [[Int]](repeating: row, count: length)
    map[length - position[1]][position[0] - 1] = -1
    var number = 0
    solve(x: 0, y: 0, size: length)
    for row in map {
        print(row.map{ String($0) }.joined(separator: " "))
    }
    
    
    func isEmpty(x: Int, y: Int, size: Int) -> Bool {
        for i in x..<x + size {
            for j in y..<y + size {
                if map[i][j] != 0 {
                    return false
                }
            }
        }
        return true
    }
    
    func solve(x: Int, y: Int, size: Int) {
        number += 1
        let newSize = size / 2
        if isEmpty(x: x, y: y, size: newSize) {
            map[x + newSize - 1][y + newSize - 1] = number;
        }
        if isEmpty(x: x + newSize, y: y, size: newSize) {
            map[x + newSize][y + newSize - 1] = number
        }
        if isEmpty(x: x + newSize, y: y + newSize, size: newSize) {
            map[x + newSize][y + newSize] =  number
        }
        if isEmpty(x: x, y: y + newSize, size: newSize) {
            map[x + newSize - 1][y + newSize] = number
        }
        
        if size == 2 { return }
        solve(x: x, y: y, size: newSize)
        solve(x: x + newSize, y: y, size: newSize)
        solve(x: x, y: y + newSize, size: newSize)
        solve(x: x + newSize, y: y + newSize, size: newSize)
    }
}
