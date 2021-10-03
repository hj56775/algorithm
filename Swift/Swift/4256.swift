//
//  4256.swift
//  PSSwift
//
//  Created by 유한준 on 2021/10/03.
//

import Foundation

func Q4256() {
    let t = Int(readLine()!)!
    for _ in 0..<t {
        let  n = Int(readLine()!)!
        let preOrder = readLine()!.split(separator: " ").map{ Int(String($0))! }
        let inOrder = readLine()!.split(separator: " ").map{ Int(String($0))! }
        var postOrder:[Int] = []
        solve(start: 0, end: n, root: 0, preOrder: preOrder, inOrder: inOrder, postOrder: &postOrder)
        print(postOrder.map{ String($0) }.joined(separator: " "))
    }
    
    func solve(start: Int, end: Int, root: Int, preOrder: [Int], inOrder: [Int], postOrder: inout [Int]) {
        for i in start..<end {
            if inOrder[i] == preOrder[root] {
                print(root,i,start)
                solve(start: start, end: i, root: root + 1, preOrder: preOrder, inOrder: inOrder, postOrder: &postOrder)
                solve(start: i + 1, end: end, root: root + i - start + 1, preOrder: preOrder, inOrder: inOrder, postOrder: &postOrder)
                postOrder.append(preOrder[root])
            }
        }
    }
}
