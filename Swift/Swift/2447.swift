//
//  2447.swift
//  PSSwift
//
//  Created by 유한준 on 2021/10/10.
//

import Foundation

func Q2447() {
    let n = Int(readLine()!)!
    let row = [String](repeating: " ", count: n)
    var map = [[String]](repeating: row, count: n)
    
    func draw(x: Int, y: Int, size: Int) {
        if size == 1 {
            map[y][x] = "*"
            return
        }
        
        let newSize = size / 3
        for i in 0..<3 {
            for j in 0..<3 {
                if i != 1 || j != 1 {
                    draw(x: x + (j * newSize), y: y + (i * newSize), size: newSize)
                }
            }
        }
    }
    
    draw(x: 0, y: 0, size: n)
    
    for row in map {
        print(row.joined())
    }
}

/* 시간 초과 ㅠ
func Q2447() {
    let n = Int(readLine()!)!
    
    func draw(x: Int, y: Int, size: Int) {
        if ( (x / size) % 3 == 1 && (y / size) % 3 == 1) {
            print(" ", terminator: "")
        }
        else if (size / 3 == 0) {
            print("*", terminator: "")
        }
        else {
            draw(x: x, y: y, size: size / 3)
        }
    }

    
    for i in 0..<n {
        for j in 0..<n {
            draw(x: i, y: j, size: n)
        }
        print()
    }
}
*/



