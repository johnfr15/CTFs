(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([[974], {
    2075: () => {}
    ,
    4356: (e, t, s) => {
        Promise.resolve().then(s.bind(s, 6482))
    }
    ,
    6482: (e, t, s) => {
        "use strict";
        s.r(t),
        s.d(t, {
            default: () => h
        });
        var a = s(5155)
          , r = s(2115);
        let n = (0,
        s(4298).io)();
        s(2075);
        let i = e => {
            let {position: t} = e;
            return (0,
            a.jsx)("img", {
                src: "/images/asteroid.png",
                alt: "asteroid",
                className: "asteroid",
                style: {
                    left: t.x,
                    top: t.y
                },
                draggable: !0
            })
        }
          , d = e => {
            let {position: t, size: s} = e;
            return (0,
            a.jsx)("img", {
                src: "/images/player.png",
                alt: "player",
                className: "player",
                style: {
                    left: t.x,
                    top: t.y,
                    width: "".concat(s.width, "px"),
                    height: "".concat(s.height, "px")
                },
                draggable: !0
            })
        }
          , c = (e, t, s) => Math.min(Math.max(e, t), s)
          , o = {
            width: 49,
            height: 40
        }
          , l = {
            width: 55,
            height: 48
        }
          , p = e => {
            let {eventTarget: t, sendPacket: s, sendPacketWithData: n} = e
              , [p,h] = (0,
            r.useState)({
                x: 50,
                y: 200
            })
              , [u,x] = (0,
            r.useState)([])
              , [g,m] = (0,
            r.useState)([])
              , [f,v] = (0,
            r.useState)(!1)
              , [w,y] = (0,
            r.useState)(0)
              , [E,b] = (0,
            r.useState)(!1)
              , [j,k] = (0,
            r.useState)("")
              , _ = () => {
                h(e => ({
                    x: 50,
                    y: c(e.y - 20, 0, 560)
                }))
            }
              , N = () => {
                h(e => ({
                    x: 50,
                    y: c(e.y + 20, 0, 560)
                }))
            }
              , S = () => {
                let e = p.y
                  , t = p.x;
                u.forEach(s => {
                    let a = s.y
                      , r = s.x;
                    r < t + o.width && r + l.width > t && a < e + o.height && l.height + a > e && L(!0)
                }
                )
            }
            ;
            function C(e) {
                switch (e.key) {
                case "z":
                    _();
                    break;
                case "s":
                    N()
                }
            }
            function O(e) {
                if (!e.detail)
                    return;
                let t = e.detail
                  , s = [];
                for (let e of t.spawns)
                    s.push({
                        x: 400,
                        y: e.y,
                        speed: e.speed
                    });
                x(e => [...e, ...s]),
                m(e => [...e, {
                    x: 400,
                    index: t.i,
                    speed: t.spawns[0].speed,
                    completed: !1
                }])
            }
            function L(e) {
                e && !f && s("game_over"),
                v(!0),
                b(!1)
            }
            function P() {
                y(e => e + 1)
            }
            function D(e) {
                e.detail && k(e.detail.flag)
            }
            return (0,
            r.useEffect)( () => {
                S()
            }
            , [p, u, f]),
            (0,
            r.useEffect)( () => {
                let e = setInterval( () => {
                    !f && E && (x(e => e.map(e => ({
                        ...e,
                        x: e.x - e.speed
                    }))),
                    x(e => e.filter(e => e.x >= -l.width * e.speed)),
                    m(e => e.map(e => ({
                        ...e,
                        x: e.x - e.speed
                    }))),
                    m(e => e.filter(e => !e.completed)))
                }
                , 30);
                return () => {
                    clearInterval(e)
                }
            }
            , [f, E]),
            (0,
            r.useEffect)( () => {
                for (let e of g)
                    !e.completed && e.x < p.x - o.width / 2 - l.width / 2 && (e.completed = !0,
                    n("wave_completed", JSON.stringify({
                        playerY: p.y,
                        waveIndex: e.index
                    })))
            }
            , [g]),
            (0,
            r.useEffect)( () => {
                if (E)
                    return document.addEventListener("keydown", C),
                    () => {
                        document.removeEventListener("keydown", C)
                    }
            }
            , [E]),
            (0,
            r.useEffect)( () => {
                t.addEventListener("wave", O),
                t.addEventListener("score_up", P),
                t.addEventListener("game_over", () => L(!1)),
                t.addEventListener("reward", D)
            }
            , []),
            (0,
            a.jsxs)("div", {
                className: "Game ".concat(f ? "game-over" : ""),
                onClick: () => {
                    f || E ? f && !E && (h({
                        x: 50,
                        y: 200
                    }),
                    x([]),
                    m([]),
                    v(!1),
                    b(!0),
                    y(0),
                    s("game_start")) : (b(!0),
                    y(0),
                    s("game_start"))
                }
                ,
                children: [(0,
                a.jsx)(d, {
                    position: p,
                    size: o
                }), u.map( (e, t) => (0,
                a.jsx)(i, {
                    position: e
                }, t)), (0,
                a.jsxs)("center", {
                    children: [(0,
                    a.jsx)("div", {
                        className: "score",
                        children: w
                    }), (0,
                    a.jsx)("div", {
                        className: "flag",
                        children: j
                    })]
                }), f && (0,
                a.jsx)("center", {
                    children: (0,
                    a.jsxs)("div", {
                        className: "game-over-message",
                        children: ["Game Over!", (0,
                        a.jsx)("br", {}), "Z to go UP, S to go DOWN", (0,
                        a.jsx)("br", {}), (0,
                        a.jsx)("p", {
                            style: {
                                backgroundColor: "blue",
                                padding: "2px 6px",
                                borderRadius: "5px"
                            },
                            children: "Click anywhere to Restart"
                        })]
                    })
                }), !E && !f && (0,
                a.jsx)("center", {
                    children: (0,
                    a.jsxs)("div", {
                        className: "game-over-message",
                        children: ["Space explorer", (0,
                        a.jsx)("br", {}), "Z to go UP, S to go DOWN", (0,
                        a.jsx)("br", {}), (0,
                        a.jsx)("p", {
                            style: {
                                backgroundColor: "blue",
                                padding: "2px 6px",
                                borderRadius: "5px"
                            },
                            children: "Click anywhere to Start"
                        })]
                    })
                })]
            })
        }
        ;
        function h() {
            let e = new EventTarget;
            return (0,
            r.useEffect)( () => (n.on("message", function() {
                for (var t = arguments.length, s = Array(t), a = 0; a < t; a++)
                    s[a] = arguments[a];
                if (0 != s.length)
                    switch (s.shift()) {
                    case "ping":
                        n.send("pong");
                        break;
                    case "message":
                        let r = JSON.parse(s[0]);
                        switch (r.event) {
                        case "new_wave":
                            e.dispatchEvent(new CustomEvent("wave",{
                                detail: r
                            }));
                            break;
                        case "game_over":
                            e.dispatchEvent(new CustomEvent("game_over"));
                            break;
                        case "score_up":
                            e.dispatchEvent(new CustomEvent("score_up"));
                            break;
                        case "reward":
                            e.dispatchEvent(new CustomEvent("reward",{
                                detail: r
                            }))
                        }
                    }
            }),
            () => {
                n.off("message")
            }
            ), []),
            (0,
            a.jsx)(p, {
                eventTarget: e,
                sendPacket: function(e) {
                    n.send(e)
                },
                sendPacketWithData: function(e, t) {
                    n.send(e, t)
                }
            })
        }
    }
}, e => {
    var t = t => e(e.s = t);
    e.O(0, [250, 298, 441, 684, 358], () => t(4356)),
    _N_E = e.O()
}
]);
