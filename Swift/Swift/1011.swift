//
//  1011.swift
//  PSSwift
//
//  Created by 유한준 on 2021/10/11.
//

import Foundation

func Q1011() {
    let t = Int(readLine()!)!
    for _ in 0..<t {
        let xAndY = readLine()!.split(separator: " ").map{ Int($0)! }
        let x = xAndY[0]
        let y = xAndY[1]
        let dist = y - x
        var i = 0
        while true {
            if (i + 1) * (i + 1) > dist{ // 1 + 2 + 3 + ... + i + i-1 + ... + 2 + 1 -> N^2
                break
            }
            else {
                i += 1
            }
        }
        let leftDist = dist - i * i
        let count = i + i - 1 + Int(ceil(Float(leftDist) / Float(i))) // 남은 거리는 i로 나눈 것을 올림하면 해결(무조건 해당하는 거리가 존재)
        
        print(count)
    }
}
