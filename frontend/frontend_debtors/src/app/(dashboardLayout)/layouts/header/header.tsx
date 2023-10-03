import { Button, Navbar } from "reactstrap";


export default function Header({ showMobmenu }: any) {
    return (
        <Navbar className="shadow-sm" light expand="md">
            <div className="d-flex align-items-center">
                <span
                    className="ms-2 d-lg-none"
                    onClick={showMobmenu}
                >
                    <Button
                        close
                        size="sm"
                    ></Button>
                </span>
            </div>
        </Navbar>
    )
}